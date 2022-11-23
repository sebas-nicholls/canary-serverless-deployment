import aws_cdk as core
import aws_cdk.assertions as assertions

from canary_serverless_deployment.canary_serverless_deployment_stack import CanaryServerlessDeploymentStack

# example tests. To run these tests, uncomment this file along with the example
# resource in canary_serverless_deployment/canary_serverless_deployment_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = CanaryServerlessDeploymentStack(app, "canary-serverless-deployment")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
