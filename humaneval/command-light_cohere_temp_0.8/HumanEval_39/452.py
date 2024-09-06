```python
def prime_fib(n: int):
    """
    prime_fib returns n-th number that is a Fibonacci number and it's also prime
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
   Golden_ratio
    >>> prime_fib(10)
    55
    >>> prime_fib(11)
    661
    """
    if n <= 1:
        return n
    if n <= 3:
        return 2
    if n % 2 == 0:
        return 3
    else:
        # n is odd, find sqrt(n^2) and divide by sqrt(n)
        sqrt_n = int(1.0 / math.sqrt(n**))
        n // sqrt_n = 4
        return 4 + prime_fib(n - 4)
```