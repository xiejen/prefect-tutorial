import prefect
from prefect import Flow, task
from prefect.run_configs import KubernetesRun
from prefect.storage import Docker

from components.componentA import ComponentA 
from components.componentB import ComponentB

FLOW_NAME = "docker_kubernetes_tutorial"
docker_storage = Docker(
    image_name="test",
    image_tag="latest",
    registry_url="de.icr.io/cogssm-dev/",
    dockerfile="./Dockerfile"
)


@task
def test_task():
    logger = prefect.context.get("logger")
    x = ComponentA(2)
    y = ComponentB(2)
    x = x.n + y.n
    logger.info(f"Test {x}!")  # Should return 4
    return

with Flow(FLOW_NAME,
          storage=docker_storage,
          run_config=KubernetesRun(
                        image="de.icr.io/cogssm-dev/test:latest",
                        labels=["k8s"],
                        image_pull_secrets=["all-icr-io"]),
    ) as flow:
    test_task()