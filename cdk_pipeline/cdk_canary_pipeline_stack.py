import aws_cdk as cdk
from aws_cdk import aws_s3 as s3
from aws_cdk.pipelines import CodePipeline, CodePipelineSource, ShellStep
from cdk_pipeline.cdk_canary_stage import CdkCanaryPipelineAppStage
from constructs import Construct

class CdkCanaryPipelineStack(cdk.Stack):
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)
        
        pipeline = CodePipeline(self, "Pipeline",
                        pipeline_name="MyCanaryPipeline",
                        synth=ShellStep("Synth",
                            input=CodePipelineSource.connection("sebas-nicholls/canary-serverless-deployment", "master",
                                connection_arn="arn:aws:codestar-connections:us-east-1:382821043170:connection/a42de134-20ca-4db4-b94e-a6c113da67f5"),
                            install_commands=["npm install -g aws-cdk"],
                            commands=["pip install -r requirements.txt", "cdk synth"]
                        )
                    )
        pipeline.add_stage(CdkCanaryPipelineAppStage(self, "CanaryDeployments",
            env=cdk.Environment(account="382821043170", region="us-east-1")))
                    