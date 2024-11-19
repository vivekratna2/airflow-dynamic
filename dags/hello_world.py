from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

dag = DAG(
    "hello_world_dag",
    schedule_interval="@once",
    catchup=False,
    start_date=datetime.now()
)

def hello_task():
    print("Hello World!")

with dag:
    task_1 = PythonOperator(
        task_id="task_1",
        python_callable=hello_task,
    )