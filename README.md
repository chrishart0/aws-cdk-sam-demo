
# Learn how to use SAM to test Lambda locally for a CDK project!

This repo shows how to locally test a Lambda function created with AWS CDK using AWS SAM. 

![how local testing works gif](static_content/sam-cdk-demo.gif)

## First setup your local environment

Ensure [AWS CDK](https://docs.aws.amazon.com/cdk/latest/guide/getting_started.html) and [AWS SAM](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-install.html) are installed. 

Clone down this repo and cd into it.

Manually create a virtualenv on MacOS and Linux:

```
$ python3 -m venv .venv
```

After the init process completes and the virtualenv is created, you can use the following
step to activate your virtualenv.

```
$ source .venv/bin/activate
```

If you are a Windows platform, you would activate the virtualenv like this:

```
% .venv\Scripts\activate.bat
```

Once the virtualenv is activated, you can install the required dependencies.

```
$ pip install -r requirements.txt
```

## Startup the Lambda function locally with SAM

Synthesize a template and write it to template.yaml

```
$ cdk synth --no-staging > template.yaml
```

Test the API with SAM

```
$ sam local start-api
```

In your browser or in another terminal hit the endpoint http://127.0.0.1:3000/. 

You can change the code of your lambda function on the fly, no need to restart SAM. Simply edit the source code in the lambda/ dir and call the endpoint again. 

## 🎉🎉🎉 Congratulations 🎉🎉🎉
You can now use this very simple strategy to test your Lambda + API Gateway in your own CDK project.