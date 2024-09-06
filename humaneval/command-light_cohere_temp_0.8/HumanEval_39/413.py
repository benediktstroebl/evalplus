```python
import math
def prime_fib(n):
    """
    prime_fib returns n-th number that is a Fibonacci number and it's also prime.
    >>> prime_fib(1) == 2
    >>> prime_fib(2) == 3
    >>> prime_fib(2) == [2, 3]
    >>> prime_fib(3) == 5
    >>> prime_fib(3) == [3, 5]
    >>> prime_fib(4) == 13
    >>> prime_fib(4) == [2, 3, 5, 13]
    >>> prime_fib(5) == 89
    """
    if n == 1:
        return 2
    elif n == 2:
        return 3
    else:
        num = math.floor(math.sqrt(n)) + 1
        if num <= 2:
            return [num]
        else:
            return [math.floor(math.sqrt(n)) + 1, num]
```