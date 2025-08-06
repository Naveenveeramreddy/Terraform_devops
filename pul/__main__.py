import pulumi
from pulumi_aws import ec2

# Define a Security Group
security_group = ec2.SecurityGroup(
    'web-sg',
    description='Enable SSH and HTTP access',
    ingress=[
        ec2.SecurityGroupIngressArgs(
            protocol="tcp",
            from_port=22,
            to_port=22,
            cidr_blocks=["0.0.0.0/0"],  # Allow SSH access
        ),
        ec2.SecurityGroupIngressArgs(
            protocol="tcp",
            from_port=80,
            to_port=80,
            cidr_blocks=["0.0.0.0/0"],  # Allow HTTP access
        ),
    ]
)

# Create an EC2 instance
ami_id = "ami-020cba7c55df1f615"  # Update with a valid Ubuntu AMI for your region
instance = ec2.Instance(
    'ubuntu-instance',
    instance_type="t3.micro",
    ami=ami_id,
    vpc_security_group_ids=[security_group.id],
    key_name="pulumi",  # Replace with your AWS key pair
    tags={
        "Name": "PulumiInstance"
    }
)
# Export the public IP of the instance
pulumi.export("public_ip", instance.public_ip)

