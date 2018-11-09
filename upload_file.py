import boto3

def get_presigned_url(file_name):
    s3Client = boto3.client('s3')
    url = s3Client.generate_presigned_url('put_object', Params={
        'Bucket': 'surfly-poc',
        'ContentType': 'image/png',
        'ACL': 'public-read',
        'Key': file_name},
        ExpiresIn=3600,
                                          HttpMethod="PUT")
    print(url)
    return url