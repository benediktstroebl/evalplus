```python
import math

def prime_fib(n):
    """
    Returns n-th number that is a Fibonacci number and it's also prime.
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
    >>> prime_fib(6)
    6
    >>> prime_fib(10)
    7
    >>> prime_fib(17)
    2340
    >>> prime_fib(19)
    86895
    """
    if n < 2:
        return n
    else:
        # To find the square root of Fibonacci number
        root = int(math.sqrt(math.pow(2, n))
        if root <= 1:
            return 2
        else:
            return root
```