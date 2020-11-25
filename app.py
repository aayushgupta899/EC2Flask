from flask import Flask
import json
import time

app = Flask(__name__)


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


if __name__ == '__main__':
    app.run()
