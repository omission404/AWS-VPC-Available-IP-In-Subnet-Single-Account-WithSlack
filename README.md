This Code will help monitor number of free ip in each subnet across single account/multiple region/vpc and alert if they decrease below specified threshold.


PLEASE NOTE, YOU CAN DEPLOY THIS CODE DIRECTLY FROM AWS CONSOLE -> Search for Available-ip and change region

https://ap-southeast-2.console.aws.amazon.com/lambda/home?region=ap-southeast-2#/create/function


####INSTRUCTIONS#####

Please follow steps to update the code as per your account numbers/arn info at specified locations.

1- In Lambda python code regionlist add all regions where you want this scan to happen

2- Create or use existing Slack app and collect the webhook url. And In Lambda python code replace the webhook url in line 24: "https://hooks.slack.com/services/..."

3- Create a Lambda Role with following permission and name it something like available-ip-single-account

	{
	    "Version": "2012-10-17",
	    "Statement": [
		{
		    "Effect": "Allow",
		    "Action": [
			"ec2:DescribeSubnets"
		    ],
		    "Resource": "*"
		},
		{
		    "Effect": "Allow",
		    "Sid": "LambdaBasicExecution",
		    "Action": [
			"logs:CreateLogGroup",
			"logs:CreateLogStream",
			"logs:PutLogEvents"
		    ],
		    "Resource": "*"
		}
	    ]
	}

4- Go to your Lambda Function Config in AWS console and change execution role name to the role name created at step 3 and test.

5- Add cloudwatch Event Cronjob to schedule lambda execution as per your required frequency Per hour/Per day etc
