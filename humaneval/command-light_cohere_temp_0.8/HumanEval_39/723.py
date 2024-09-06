```python
import math

def prime_fib(n):
    """
    returns n-th number that is a Fibonacci number and it's also prime
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
    165
    >>> prime_fib(10)
    33454
    >>> prime_fib(55)
    333886
    """
    if n <= 1:
        return n
    if n <= 3:
        return 3
    if n % 2 == 0:
        return 5
    i = 5
    while i * i <= n:
        if n % (i + 2) == 0:
            break
        i += 6
    return i
```