import logging
import argparse
import boto3
from botocore.exceptions import ClientError

parser = argparse.ArgumentParser (description='s3-bucket-create')
parser.add_argument('bucketname', type=str, nargs=1,help= 'please enter a name for oyour bucket')
parser.add_argument('region', nargs=1, help= 'The AWS region the bucket will be created in' )
parser.add_argument('--public',default=False,action='store_true', help= 'do you need the bucket permission open or closed, recomendation is to always keep you bucket closed for security.')
args = parser.parse_args()

def create_bucket(bucket_name, region):
    try:
        s3_client = boto3.client('s3')
        location = {'LocationConstraint': region}
        s3_client.create_bucket(Bucket=bucket_name, CreateBucketConfiguration=location)
    except ClientError as e:
        logging.error(e)
        return False
    return True


def make_private(bucket_name):
    s3_client = boto3.client('s3')
    try:
        response_public = s3_client.put_public_access_block(
            Bucket=bucket_name,
            PublicAccessBlockConfiguration={
                'BlockPublicAcls': True,
                'IgnorePublicAcls': True,
                'BlockPublicPolicy': True,
                'RestrictPublicBuckets': True
            }
        )
    except ClientError as e:
        logging.error(e)
        return False
    return True


s3_output=create_bucket(args.bucketname[0], args.region[0])
if s3_output == True:
    print('s3 bucket '+ args.bucketname[0] + ' is created')
if args.public == False:
    make_private(args.bucketname[0])
else:
    print('WARNING bucket permission are open')



