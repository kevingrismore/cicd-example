from prefect import flow

@flow(log_prints=True)
def hello():
  print("Hello!")