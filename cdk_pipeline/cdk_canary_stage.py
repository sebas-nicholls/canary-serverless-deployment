import aws_cdk as cdk
from constructs import Construct

from canary_serverless_deployment.canary_serverless_deployment_stack import CanaryServerlessDeploymentStack

class CdkCanaryPipelineAppStage(cdk.Stage):
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        application_stack = CanaryServerlessDeploymentStack(self, "CanaryServerlessDeploymentStack")