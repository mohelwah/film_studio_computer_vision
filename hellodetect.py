import boto3

def detect(bucket, name):
    rekognition = boto3.client('rekognition')
    print(f'this is bucket {bucket}, this is name {name}')

detect('foo', 'boo')