from aws_cdk import (
    # Duration,
    Stack,
    aws_s3 as s3,
    aws_ec2 as ec2,
    aws_rds as rds,
    aws_dynamodb as dynamodb, 
)
from constructs import Construct

class SecondcaseStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # The code that defines your stack goes here

        s3.Bucket(self,"sitebucket",bucket_name="case2bucket81",public_read_access=True,
        website_index_document="index.html")

        vpc = ec2.Vpc(self, "STACKVPC")

        rds.DatabaseInstance(
            self, "STACKRDS",
            database_name="GLUEDB",
            engine=rds.DatabaseInstanceEngine.mysql(
                version=rds.MysqlEngineVersion.VER_5_7
            ),
            vpc=vpc,
            port=3306,
            instance_type= ec2.InstanceType.of(
                ec2.InstanceClass.BURSTABLE2,
                ec2.InstanceSize.MICRO,
            ),
            deletion_protection=False
        ),

        dynamodb.Table(
            self, "stack_table",
            partition_key=dynamodb.Attribute(
                name="id",
                type=dynamodb.AttributeType.STRING
            )
        )
