```python
def prime_fib(n: int):
    """
    Returns n-th number that is a Fibonacci number and it's also prime.
    Returns the general Fibonacci number.
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
    24
    >>> prime_fib(7)
    50
    >>> prime_fib(8)
    128
    >>> prime_fib(9)
    521
    >>> prime_fib(10)
    34359089
    """
    if n <= 1:
        return n
    if n % 2 == 0:
        return prime_fib(n // 2) + prime_fib(n // 2)
    else:
        return prime_fib(n // 2) + prime_fib(n // 2) + (prime_fib(n // 2) * prime_fib(n // 2))
```