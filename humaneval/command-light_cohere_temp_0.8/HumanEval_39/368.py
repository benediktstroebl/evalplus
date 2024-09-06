```python
import math

def prime_fib(n):
    """
    Returns n-th Fibonacci number and it's also prime.
    if n <= 1:
        return n
    if n % 2 == 0:
        return 2
    fib = 0
    fib += 1
    while fib < n:
        fib *= fib + 1
    return fib

def test_prime_fib(x):
    assert prime_fib(5) == 89
```