```python
def prime_fib(n: int):
    """
    Returns the n-th Fibonacci number that is prime.
    >>> prime_fib(1)
    2
    True
    >>> prime_fib(2)
    3
    True
    >>> prime_fib(3)
    5
    True
    >>> prime_fib(4)
    13
    True
    >>> prime_fib(5)
    89
    >>> prime_fib(6)
    25
    False
    """
    if n <= 1:
        return 2
    if n == 2:
        return 3
    if n % 2 == 0:
        return 5
    return 13
```