import time
import os


if __name__ == "__main__":
    print("                   Hello, world!")
    
    for k, v in os.environ.items():
        print(f'{k}={v}')


