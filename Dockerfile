FROM apache/airflow:2.10.3-python3.12

ENV PYTHONPATH "${PYTHONPATH}:/opt/airflow/jobs"
ENV PYTHONPATH "${PYTHONPATH}:/opt/airflow/core"
ENV PYTHONPATH "${PYTHONPATH}:/opt/airflow/tasks"
ENV PYTHONPATH "${PYTHONPATH}:/opt/airflow/workflows"

COPY ./setup.py ./setup.py
RUN pip3 install --upgrade pip && pip3 install --no-cache-dir --compile --editable .

USER root
RUN apt-get update && apt-get install wget -y && apt-get install telnet -y
RUN apt-get install traceroute -y

USER airflow
