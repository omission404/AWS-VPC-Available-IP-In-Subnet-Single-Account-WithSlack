import json
import boto3
import urllib3
 
 
def lambda_handler(event, context):
        regionlist=['ca-central-1','us-east-1']  # --> Change Number 1
        notification = ""
        for region in regionlist:
            ec2 = boto3.client('ec2',region_name=region)
            output_describe_subnets = ec2.describe_subnets(Filters=[{'Name': 'state', 'Values': ['available']}])
            print(output_describe_subnets)
            for eachsubnet in output_describe_subnets['Subnets']:
                message = "Available IP's in Account Number: %s , Region: %s, VPC ID: %s , Subnet: %s has a total of  %d remaining IPs" % (eachsubnet['OwnerId'],region,eachsubnet['VpcId'],eachsubnet['SubnetId'], eachsubnet['AvailableIpAddressCount'])
                if eachsubnet['AvailableIpAddressCount']<15: # Feel free to change this number from 10 to any number on which you want to be alerted
                    print(message)
                    notification = notification+"\n"+message
                     
                    if notification:
                        http = urllib3.PoolManager()
                        print(notification)
                        data = {"text": message}
                        r = http.request("POST",
                        "https://hooks.slack.com/services/..."#[Webhook URL from your slack app],
                        body = json.dumps(data),
                        headers = {"Content-Type": "application/json"})
