import boto3
import json

def handler(event, context):

    gordon_context = json.loads(open('.context', 'r').read())
    print(gordon_context['vpn_endpoint'])
    
    ubuntu_ami = gordon_context['ami_for_vpn_client']
    user_data_template = open('cloud-init.yml', 'r').read()


    user_data = user_data_template.format({
        'vpn_endpoint': gordon_context['vpn_endpoint'] 
    })

    client = boto3.client('ec2', region_name=gordon_context['aws_region'])
    client.run_instances(
        ImageId=ubuntu_ami,
        MinCount=1,
        MaxCount=1,
        InstanceType='t2.nano',
        InstanceInitiatedShutdownBehavior='terminate',
        UserData=user_data,
        KeyName='soenke',
        SecurityGroupIds=gordon_context['vpn_client_security_groups'],
    )


if __name__ == "__main__":
    handler({}, {})

