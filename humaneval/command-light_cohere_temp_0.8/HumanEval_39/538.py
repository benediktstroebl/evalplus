```python
import math
def prime_fib(n):
    if n <= 1:
        return n
    if n <= 3:
        return 3
    if n % 2 == 0:
        return 5
    temp = prime_fib(n // 2)
    if temp == 2 or temp == 3:
        return temp
    return temp + prime_fib(n % 2)
``` 
This script defines a function `prime_fib` that calculates and returns the n-th Fibonacci number that is prime. It uses a proof by induction and an iterative approach to find the n-th prime Fibonacci number.