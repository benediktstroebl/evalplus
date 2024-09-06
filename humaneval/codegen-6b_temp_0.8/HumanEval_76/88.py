
def is_simple_power(x, n):
    """Your task is to write a function that returns true if a number x is a simple
    power of n and false in other cases.
    x is a simple power of n if n**int=x
    For example:
    is_simple_power(1, 4) => true
    is_simple_power(2, 2) => true
    is_simple_power(8, 2) => true
    is_simple_power(3, 2) => false
    is_simple_power(3, 1) => false
    is_simple_power(5, 3) => false
    """
    if n == 1:
        return x == 1
    elif n == 2:
        return x == 2
    elif x < n:
        return x**(n-1) == n
    else:
        return x%n == 0

import time
start = time.time()
m = 100000
for i in range(1, m):
    if is_simple_power(i, 3) and is_simple_power(i, 5) and is_simple_power(i, 7):
        print(i)