import streamlit as st
import pandas as pd
import numpy as np
from collections import Counter
import matplotlib.pyplot as plt
import pandas_bokeh
import missingno

st.set_page_config(page_icon=":bar_chart:", page_title="EDA Automation  -- Animesh Bhatt")


# Creating the functions for each operation

def data_corr_chart(corr_df):
    fig = plt.figure(figsize=(15, 15))
    plt.imshow(corr_df.values, cmap="Reds")
    plt.xticks(range(corr_df.shape[0]), corr_df.columns, rotation=90, fontsize=15)
    plt.yticks(range(corr_df.shape[0]), corr_df.columns, fontsize=15)
    plt.colorbar()

    for i in range(corr_df.shape[0]):
        for j in range(corr_df.shape[0]):
            plt.text(i, j, "{:.2f}".format(corr_df.values[i, j]), color="black", ha="center", fontsize=14,
                     fontweight="bold")

    return fig


def missing_values_bar(df):
    missing_fig = plt.figure(figsize=(10, 5))
    ax = missing_fig.add_subplot(111)
    missingno.bar(df, figsize=(10, 5), fontsize=12, ax=ax)

    return missing_fig


def cat_cont_columns(df):  ## Logic to Separate Continuous & Categorical Columns
    cont_columns = []
    cat_columns = []
    for col in df.columns:
        if len(df[col].unique()) <= 25 or df[col].dtype == np.object_:  ## If less than 25 unique values
            cat_columns.append(col.strip())
        else:
            cont_columns.append(col.strip())
    return cont_columns, cat_columns


# Creating the web app

st.title("EDA Automation Using Python :bar_chart::chart_with_upwards_trend:")
st.caption(
    "Upload CSV file to see various Charts related to EDA. Please upload file that has both continuous columns and categorical columns.",
    unsafe_allow_html=True)
upload = st.file_uploader(label="Upload File Here:", type=["csv"])

if upload:
    data = pd.read_csv(upload)

    tab1, tab2, tab3 = st.tabs(["Dataset Overview :clipboard:", "Individual Column Stats :bar_chart:",
                                "Explore Relation Between Features :chart:"])

    with tab1:
        st.subheader("1. Dataset")
        st.write(data)

        cont_columns, cat_columns = cat_cont_columns(data)

        st.subheader("2. Data Overview")

        st.markdown("<span style='font_weight :bold;'>{}</span> : {}".format("Row", data.shape[0]),
                    unsafe_allow_html=True)
        st.markdown("<span style ='font_weight:bold;'>{}</span> : {}".format("Duplicates", data.shape[0] -
                                                                             data.drop_duplicates().shape[0]),
                    unsafe_allow_html=True)
        st.markdown("<span style='font-weight:bold;'>{}</span> : {}".format("Features", data.shape[1]),
                    unsafe_allow_html=True)
        st.markdown("<span style='font-weight:bold;'>{}</span> : {}".format("Categorical Columns", len(cat_columns)),
                    unsafe_allow_html=True)
        st.write(cat_columns)
        st.markdown("<span style='font-weight:bold;'>{}</span> : {}".format("Continuous Columns", len(cont_columns)),
                    unsafe_allow_html=True)
        st.write(cont_columns)

        corr_df = data[cont_columns].corr()
        corr_fig = data_corr_chart(corr_df)

        st.subheader("3. Correlation Chart")
        st.pyplot(corr_fig, use_container_width=True)

        st.subheader("4. Missing Values Distribution")
        missing_fig = missing_values_bar(data)
        st.pyplot(missing_fig, use_container_width=True)

    with tab2:
        data_descr = data.describe()
        st.subheader("Analyze Individual Feature Distribution")

        st.markdown("#### 1. Understand Continuous Feature")
        feature = st.selectbox(label="Select Continuous Feature", options=cont_columns, index=0)

        na_cnt = data[feature].isna().sum()
        st.markdown("<span style='font-weight:bold;'>{}</span> : {}".format("Count", data_descr[feature]['count']),
                    unsafe_allow_html=True)
        st.markdown("<span style='font-weight:bold;'>{}</span> : {} / ({:.2f} %)".format("Missing Count", na_cnt,
                                                                                         na_cnt / data.shape[0]),
                    unsafe_allow_html=True)
        st.markdown("<span style='font-weight:bold;'>{}</span> : {:.2f}".format("Mean", data_descr[feature]['mean']),
                    unsafe_allow_html=True)
        st.markdown("<span style='font-weight:bold;'>{}</span> : {:.2f}".format("Standard Deviation",
                                                                                data_descr[feature]['std']),
                    unsafe_allow_html=True)
        st.markdown("<span style='font-weight:bold;'>{}</span> : {}".format("Minimum", data_descr[feature]['min']),
                    unsafe_allow_html=True)
        st.markdown("<span style='font-weight:bold;'>{}</span> : {}".format("Maximum", data_descr[feature]['max']),
                    unsafe_allow_html=True)
        st.markdown("<span style='font-weight:bold;'>{}</span> :".format("Quantiles"), unsafe_allow_html=True)
        st.write(data_descr[[feature]].T[['25%', "50%", "75%"]])
        ## Histogram
        hist_fig = data.plot_bokeh.hist(y=feature, bins=50, legend=False, vertical_xlabel=True, figsize=(600, 500),
                                        show_figure=False)
        st.bokeh_chart(hist_fig, use_container_width=True)

        st.markdown("#### 2. Understand Categorical Feature")
        feature = st.selectbox(label="Select Categorical Feature", options=cat_columns, index=0)
        ### Categorical Columns Distribution        
        cnts = Counter(data[feature].values)
        df_cnts = pd.DataFrame({"Type": cnts.keys(), "Values": cnts.values()})
        bar_fig = df_cnts.plot_bokeh.bar(x="Type", y="Values", color="tomato", legend=False, show_figure=False)
        st.bokeh_chart(bar_fig, use_container_width=True)

    with tab3:
        st.subheader("Explore Relationship Between Features of Dataset")

        col1, col2 = st.columns(2)

        with col1:
            x_axis = st.selectbox(label="X-Axis", options=cont_columns, index=0)
        with col2:
            y_axis = st.selectbox(label="Y-Axis", options=cont_columns, index=1)

        color_encode = st.selectbox(label="Color-Encode", options=[None, ] + cat_columns)

        scatter_fig = data.plot_bokeh.scatter(x=x_axis, y=y_axis, category=color_encode if color_encode else None,
                                              title="{} vs {}".format(x_axis.capitalize(), y_axis.capitalize()),
                                              figsize=(600, 500), fontsize_title=20, fontsize_label=15,
                                              show_figure=False)
        st.bokeh_chart(scatter_fig, use_container_width=True)











