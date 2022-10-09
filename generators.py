
import time


def simple_generator():
    print('FIRST VAL ')
    time.sleep(4)
    yield 1
    print('SECOND VAL ')
    time.sleep(2)
    yield 2
    print('THIRD VAL ')
    time.sleep(7)
    yield 3


for val in simple_generator():
    print(val)