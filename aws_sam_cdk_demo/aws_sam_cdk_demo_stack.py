from aws_cdk import core as cdk
from aws_cdk import (
    core,
    aws_lambda as _lambda,
    aws_apigateway as apigateway,
)

class AwsSamCdkDemoStack(cdk.Stack):

    def __init__(self, scope: cdk.Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        #https://docs.aws.amazon.com/cdk/api/latest/python/aws_cdk.aws_lambda_python/README.html
        greeting_function = _lambda.Function(
            self, 'greeting_handler',
            runtime=_lambda.Runtime.PYTHON_3_9,
            code=_lambda.Code.asset('lambda'),
            handler='greeting_generator.handler',
        )

        #https://docs.aws.amazon.com/cdk/api/latest/python/aws_cdk.aws_apigateway/README.html
        greeting_apg = apigateway.LambdaRestApi(
            self, 'greeting_endpoint',
            handler=greeting_function,
            description="Greeting API endpoint",
        )