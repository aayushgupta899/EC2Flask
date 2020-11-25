from flask import Flask
from flask import send_file
import boto3
import json
import time

app = Flask(__name__)

AWS_ACCESS_KEY_ID = ''
AWS_SECRET_ACCESS_KEY = ''

@app.route('/')
def hello():
    return "Hello World!"


@app.route('/compute')
def compute():
    start = time.process_time()
    n = 3684059
    isPrime = True
    if n <= 1 or n % 1 > 0:
        isPrime = False
    for i in range(2, n // 2):
        if n % i == 0:
            isPrime = False
    end = time.process_time()
    return {
        'statusCode': 200,
        'compute': str(end - start),
        'result': str(isPrime)
    }


@app.route('/get_image')
def get_image():
    s3 = boto3.client('s3', aws_access_key_id=AWS_ACCESS_KEY_ID, aws_secret_access_key=AWS_SECRET_ACCESS_KEY)
    s3.download_file('deep-learning-inference', 'download.jfif', 'test.jfif')
    n = 99173
    isPrime = True
    if n <= 1 or n % 1 > 0:
        isPrime = False
    for i in range(2, n // 2):
        if n % i == 0:
            isPrime = False
    return send_file('test.jfif', mimetype='image/jfif')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
