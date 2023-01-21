#import boto3

def detect(bucket, name):
    #rekognition = boto3.client('rekognition')
    print(f'this is bucket {bucket}, this is name {name}')

file = 's3://film-studio-computer-vision-2023/lebron-lakers.jpg'
detect('foo', 'boo')