# Data Pipeline ETL

This project implements a simple ETL (Extract, Transform, Load) pipeline using **Apache Airflow**, **Pandas**, and **Snowflake** to clean, transform, and load data from a CSV file into Snowflake.

## Features

- **Extract**: Reads data from a CSV file.
- **Transform**: Cleans and processes the data, including removing missing values, and applying business logic like filtering based on age.
- **Load**: Loads the cleaned and transformed data into **Snowflake** for further analysis.
- **Orchestration**: The pipeline is managed by **Apache Airflow**, which schedules and tracks the workflow steps.

## Requirements

Before running this project, make sure you have the following installed:
- **Python** (>=3.8)
- **Apache Airflow** (for orchestration)
- **Snowflake** (for data storage)
- **Git** (for version control)
- **Pandas** (for data manipulation)
- **Docker** (optional, for containerized environments)

You can set up your environment by following these steps.

### Step-by-Step Setup

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/data_pipeline.git
   
2. Create a Python virtual environment:

bash
Copy code
python3 -m venv venv
source venv/bin/activate  # For Windows, use `venv\Scripts\activate`

3. Install dependencies:

bash
Copy code
pip install -r requirements.txt

4. Configure Snowflake credentials: Set up your Snowflake credentials as environment variables or via configuration files. Example:

bash
Copy code
export SNOWFLAKE_USER='your_username'
export SNOWFLAKE_PASSWORD='your_password'
export SNOWFLAKE_ACCOUNT='your_account_url'

5. Start Airflow:

Initialize the Airflow database:
bash
Copy code
airflow db init
Start the web server and scheduler:
bash
Copy code
airflow webserver --port 8080
airflow scheduler

6. Run the DAG:

Visit Airflow's web UI at http://localhost:8080 to manually trigger the ETL job.
ETL Process Flow
1. Extract:

The extract task reads the input data from a CSV file located at data/people-10000.csv.

2. Transform:

The transform task cleans and processes the data, including removing rows with missing values and applying logic (e.g., filtering based on age, creating additional flags).
Load:

The load task pushes the cleaned data to Snowflake for further processing and analysis.
Data Pipeline Overview
Extract: This part reads data from a CSV file into a Pandas DataFrame.
Transform: Cleans the data by removing any rows with missing values and adding business-specific transformations, such as filtering data based on age and adding flags (e.g., is_adult).

3. Load: Once the data is transformed, it is loaded into Snowflake for further storage and querying.
Sample CSV File
The pipeline starts by processing the following sample data:

User Id	Name	Age	Date of Birth	Job Title
1	John Doe	25	1999-02-15	Software Engineer
2	Jane Smith	30	1994-04-21	Data Scientist
3	Alice Brown	17	2007-11-02	Student
The transformations include:

Removing any rows with missing values.
Creating a new column (is_adult) that marks whether a person is an adult (age 18 and above).
Filtering the data to include only adults.

Contributing
We welcome contributions to this project! To contribute:

1. Fork the repository.
2. Clone your forked repository:
bash
Copy code
git clone https://github.com/yourusername/data_pipeline.git

4. Create a new branch:
bash
Copy code
git checkout -b feature/your-feature-name
Make changes and commit them:
bash
Copy code
git commit -m "Implemented new feature"

5. Push to your fork:
bash
Copy code
git push origin feature/your-feature-name

6. Open a pull request from your fork to the main repository.
License
This project is licensed under the MIT License - see the LICENSE file for details.

Acknowledgements
Apache Airflow: Used for workflow orchestration.
Snowflake: A cloud-based data warehouse that serves as the final destination for the processed data.
Pandas: Used for data manipulation and transformation.
