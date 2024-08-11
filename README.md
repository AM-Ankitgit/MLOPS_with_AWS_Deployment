# MLOPS_with_AWS_Deployment
creating project from scratched to implement the MLOPs with Deployment on AWS





### dagshub
mlflow tracking url  (this url is getting set by dagshub)

in windows set url and you can see the dashboard of mlflow

set MLFLOW_TRACKING_URI=https://dagshub.com/AM-Ankitgit/MLOPS_with_AWS_Deployment.mlflow

set MLFLOW_TRACKING_USERNAME=AM-Ankitgit

set MLFLOW_TRACKING_PASSWORD=9a0cfdb8c9f9890d8d9e80455ae5918fcb9f4cb6


import dagshub
dagshub.init(repo_owner='AM-Ankitgit', repo_name='MLOPS_with_AWS_Deployment', mlflow=True)

import mlflow
with mlflow.start_run():
  mlflow.log_param('parameter name', 'value')
  mlflow.log_metric('metric name', 1)
