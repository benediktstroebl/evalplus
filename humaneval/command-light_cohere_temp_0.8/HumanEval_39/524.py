```python
import math

def is_prime(n):
    """
    Check if n is a prime number.
    If n is 1 or 2, it returns False
    otherwise, check if n is divisible by any number in these ranges:
    for i in range(2,int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def prime_fib(n):
    """
    Returns n-th number that is a Fibonacci number and it's also prime.
    if n < 1:
        return 2
    elif is_prime(n):
        return n + prime_fib(n - 1)
    else:
        return prime_fib(n)

print(prime_fib(10))
```