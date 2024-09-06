```python
import math

def prime_fib(n):
    if n <= 0:
        raise ValueError("Input must be a positive integer")
    if n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        a, b = 1, 2
        for _ in range(3, n + 1):
            a, b = b, a + b + math.math.fib(a)
 prime_fib(n - 1)
``` 
This code defines a `prime_fib` function that computes the nth Fibonacci number that is prime and returns it. 

The function uses a loop to check for prime numbers in the Fibonacci sequence up to the nth number.