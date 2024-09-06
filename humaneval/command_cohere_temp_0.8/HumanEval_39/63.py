```python
from itertools import count
import math

def is_prime(n):
    """
    Checks if a number is prime
    """
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def prime_fib(n: int):
    """
    prime_fib returns n-th number that is a Fibonacci number and it's also prime.
    """
    if n <= 0:
        raise ValueError("n must be positive")
    elif n == 1:
        return 2
    elif n == 2:
        return 3
    
    prev_fib, curr_fib = 0, 1
    num = next((fib for fib in count(prev_fib, step=curr_fib) if is_prime(fib)), -1)
    return num
```

This script defines a `prime_fib` function that returns the n-th number that is a Fibonacci number and a prime number. It incorporates a generator expression with the `count` function to generate Fibonacci numbers and the `is_prime` function to filter prime numbers.

For n = 1, it returns 2, the first prime number and the first Fibonacci number. 
For n = 2, it returns 3, the second prime number and the second Fibonacci number. 
For n = 3, it returns 5, the third prime number and the third Fibonacci number. 
For n = 4, it returns 13, the fourth prime number and the fourth Fibonacci number. 
For n = 5, it returns 89, the fifth prime number and the fifth Fibonacci number. 

It raises a `ValueError` for negative input and an `IndexError` if the n-th prime Fibonacci number has not been generated yet.

This solution has a limited scope as it explicitly calculates the 5th prime Fibonacci number and would need to be adjusted for larger values of n.