# s3-bucket-creation
Q29tcGlsZWQgYnkgRGV2T3BzLUNvZGll

## What am I
I am a tool that creates s3 buckets in aws, I'm written in python and use boto3, written by devops-codie.
I can create s3 buckets and accept args like bucketname(name of the bucket), region(aws region you would like the bucket located), and public(by default im built to create s3 buckets with no public permissions, but in the case you need to host your website on s3 you can apply the --public argument.

## How to use me 

You can build me into a docker image with the command below 
```sh
docker build -t s3-create-bucket .
```
To run me use the command below, by default I lock down s3, if you dont specify the --public args.
```sh
docker run --rm -ti -v ~/.aws:/root/.aws s3-create-bucket name-of-the-s3-bucket aws-region 
```

Add the --public argument if you need to have your s3 bucket with open permissions (Bad), but i like to give options.
```sh
docker run --rm -ti -v ~/.aws:/root/.aws s3-create-bucket name-of-the-s3-bucket aws-region --public
```
