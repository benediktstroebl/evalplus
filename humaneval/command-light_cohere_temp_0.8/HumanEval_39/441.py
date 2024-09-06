```python
import math
def prime_fib(n):
    """
    Returns n-th Fibonacci number that is also prime.
    >>> prime_fib(1)
    2
    >>> prime_fib(2)
    3
    >>> prime_fib(3)
    5
    >>> prime_fib(4)
    13
    >>> prime_fib(5)
    89
    >>> prime_fib(10)
    2985
    >>> prime_fib(15)
    52711
    >>> prime_fib(20)
    8000099
"""
    if n <= 1:
        return n
    elif n <= 3:
        return 2
    elif n % 2 == 0:
        return prime_fib(n - 2)
    else:
        # Find sqrt(n^2)
        sqrt_n = math.sqrt(n **sqrt_n)
        i = 4
        while i * i <= sqrt_n:
            if n % i == 0:
                break
            i += 1
        else:
            # n is a prime number
            return n

        else:
            # n is not a prime, return next prime number
            return prime_fib(n + 2)
```
The function will return the n-th Fibonacci number that is prime.