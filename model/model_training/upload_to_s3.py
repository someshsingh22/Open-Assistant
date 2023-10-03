import boto3
import os

def upload(upload_type, path, project_name):
    s3_info={"AWS_ACCESS_KEY_ID":os.getenv("AWS_ACCESS_KEY_ID"),"AWS_SECRET_ACCESS_KEY":os.getenv("AWS_SECRET_ACCESS_KEY"),"AWS_BUCKET":"crawldatafromgcp","AWS_BUCKET_FOLDER":f"somesh/{project_name}"}
    s3_client = boto3.client('s3', aws_access_key_id=s3_info["AWS_ACCESS_KEY_ID"], aws_secret_access_key=s3_info["AWS_SECRET_ACCESS_KEY"])
    transfer = boto3.s3.transfer.S3Transfer(s3_client)
    if upload_type == 0:
        for root,dirs,files in os.walk(path):
            for file in files:
                transfer.upload_file(os.path.join(root,file),s3_info["AWS_BUCKET"],s3_info["AWS_BUCKET_FOLDER"]+'/'+os.path.join(root,file))
    else:
        s3_flname= path.split(os.sep)[-1]
        print(s3_flname)
        transfer.upload_file(path,s3_info["AWS_BUCKET"],s3_info["AWS_BUCKET_FOLDER"]+'/'+s3_flname)