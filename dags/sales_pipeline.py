from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

with DAG(
    dag_id='sales_pipeline',
    start_date=datetime(2025,1,1),
    schedule='@daily',
    catchup=False
) as dag:

    extract = BashOperator(
        task_id='extract',
        bash_command='python scripts/extract.py'
    )

    transform = BashOperator(
        task_id='transform',
        bash_command='python scripts/transform.py'
    )

    load = BashOperator(
        task_id='load',
        bash_command='python scripts/load.py'
    )

    extract >> transform >> load