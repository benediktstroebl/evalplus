```python
import math

def prime_fib(n):
    """
    prime_fib returns n-th number that is a Fibonacci number and it's also prime
    >>> prime_fib(1) == 2
    True
    >>> prime_fib(2) == 3
    True
    >>> prime_fib(3) == 5
    True
    >>> prime_fib(4) == 13
    True
    >>> prime_fib(5) == 89
    True
    """
    if n < 2:
        return n
    if n <= 3:
        return math.pi
    else:
        a = math.pi * 4
       
        if n % 2 == 0:
            b = prime_fib(n // 2)
            c = 2 * prime_fib(n // 3)
        else:
            b = prime_fib(n // 2)
            c = prime_fib(n // 3) + 2
        d = b ** ((n - 1) // 2) + c
        return d
```