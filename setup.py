from setuptools import find_packages, setup

requirements = [
    "apache-airflow==2.10.3"
]

setup(
    name="Airflow-Dynamic",
    version="1.0",
    description="Dynamic Dags Generation in Airflow",
    author="Vivek Ratna Kansakar",
    author_email="kansakar.vivek@gmail.com",
    packages=find_packages(),
    install_requires=requirements,
    extras_require={
    },
)
