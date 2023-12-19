from prefect import flow


@flow(log_prints=True)
def hello():
    print("Hello!")


if __name__ == "__main__":
    hello.deploy(
        name="my-deployment",
        work_pool_name="my-work-pool",
        image="kevingrismoreprefect/cicd-example:latest",
    )
