from airflow.decorators import task, dag
from airflow.utils.dates import days_ago
import pandas as pd

# Define the DAG
@dag(schedule_interval=None, start_date=days_ago(1), catchup=False)
def etl_people_data_dag():
    @task()
    def extract():
        """
        Extract task: Reads data from the CSV file.
        """
        # File path to the dataset
        file_path = "/usr/local/airflow/dags/data/people-10000.csv"

        # Read the CSV file
        df = pd.read_csv(file_path)

        # Return the DataFrame as a JSON-like dictionary for further processing
        return df.to_dict(orient='records')

    @task()
    def transform(data):
        """
        Transform task: Cleans and filters the data.
        """
        # Convert list of dictionaries back to a DataFrame
        df = pd.DataFrame(data)

        # 1. Drop rows with missing or null values
        df = df.dropna()

        # 2. Standardize email addresses (lowercase)
        if 'email' in df.columns:
            df['email'] = df['email'].str.lower()

        # 3. Format phone numbers to a consistent style (example: (XXX) XXX-XXXX)
        if 'phone' in df.columns:
            df['phone'] = df['phone'].str.replace(r'\D', '', regex=True)  # Remove non-numeric characters
            df['phone'] = df['phone'].apply(lambda x: f"({x[:3]}) {x[3:6]}-{x[6:]}" if len(x) == 10 else x)

        # 4. Remove duplicates
        df = df.drop_duplicates()

        # 5. Normalize job titles to title case
        if 'job_title' in df.columns:
            df['job_title'] = df['job_title'].str.title()

        # 6. Add an 'age' column based on 'date_of_birth' (if present)
        if 'date_of_birth' in df.columns:
            df['date_of_birth'] = pd.to_datetime(df['date_of_birth'], errors='coerce')
            df['age'] = (pd.Timestamp.now() - df['date_of_birth']).dt.days // 365
            df = df[df['age'] >= 18]  # Filter out minors

        # Return the transformed DataFrame as a JSON-like dictionary
        return df.to_dict(orient='records')

    @task()
    def load(transformed_data):
        """
        Load task: Saves the transformed data to a new CSV file.
        """
        # Convert list of dictionaries back to a DataFrame
        df = pd.DataFrame(transformed_data)

        # Define the output path
        output_path = "/usr/local/airflow/dags/data/transformed_people.csv"

        # Save the DataFrame to a new CSV file
        df.to_csv(output_path, index=False)

        print(f"Transformed data saved to {output_path}")

    # Task dependencies
    raw_data = extract()
    transformed_data = transform(raw_data)
    load(transformed_data)

# Instantiate the DAG
etl_people_data_dag = etl_people_data_dag()
