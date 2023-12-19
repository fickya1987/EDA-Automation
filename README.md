# Atomated_EDA:
App URL: https://emilyautomatededa.streamlit.app/  

Aims to automate the Exploratory Data Analysis (EDA) process using Python and Streamlit.  The automation involves creating a Streamlit web application that allows users to upload a CSV file, and subsequently generates various charts and statistics to provide insights into the dataset.
# Introduction
Exploratory Data Analysis (EDA) is a crucial phase in the data analysis process that involves the initial exploration, visualization, and understanding of a dataset before diving into more complex analyses or modeling. EDA plays a pivotal role in revealing patterns, trends, and insights hidden within the data, helping analysts and data scientists make informed decisions.

During EDA, we examine  the distribution of variables, identify outliers, explore relationships between features, and gain a comprehensive overview of the dataset's characteristics. Traditionally, EDA has been a manual and time-intensive task, requiring analysts to create numerous plots, conduct statistical tests, and iteratively explore the data to gain insights.

However, with the advent of technology and the rise of automation tools, there has been a paradigm shift in how EDA is performed. Automating the EDA process offers several benefits, transforming it into a more efficient and scalable operation.
# Methodology
## Part 1: Create functions to perform specific EDA operations
Step 1:  Generate a correlation chart for continuous columns.<br>
Step 2: Create a bar chart to visualize missing values in the dataset.<br>
Step 3: Separate continuous and categorical columns in the dataset.<br>
## Part 2: Create Streamlit Web App<br>
> **Step 1: Set up streamlit app**  <br>
>
>> * Set the configuration for the Streamlit page, defining the page icon and title  <br>
>> * Set up the Streamlit web app by defining the title and a file uploader for CSV files.  <br>
>> * If a file is uploaded, read the data and create tabs for different EDA sections.  <br>
>
> **Step 2: Dataset Overview Tab**  <br>
>
>> * Display basic information about the dataset, including the number of rows, duplicates, features, categorical columns, and continuous columns.  <br>
>> * Generate a correlation chart for continuous columns.  <br>
>> * Create a bar chart to visualize missing values distribution in the dataset  <br>
>
> **Step 3: Individual Column Stats Tab** <br>
>
>> * Display descriptive statistics for selected continuous features.  <br>
>> * Show a histogram for the selected continuous feature.  <br>
>> * Visualize the distribution of values for selected categorical features using a bar chart.  <br>
>
> **Step 4: Explore Relation Between Features Tab**  <br>
>
>> * Allow users to select features for the X-axis, Y-axis, and color-encoding in a scatter plot.  <br>
>> * Generate an interactive scatter plot to explore relationships between selected features.  <br>




