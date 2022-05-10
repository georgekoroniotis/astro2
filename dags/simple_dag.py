from airflow import DAG

with DAG('simple_dag',
        start_date = '2022-05-15',
        schedule_interval = None,
        end_date = None,
    ) as dag:
    None