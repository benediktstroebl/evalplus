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
    24
    >>> prime_fib(10)
    973681
    >>> prime_fib(15)
    4790099
    """
    if n <= 1:
        return n
    if n <= 3:
        return 2
    if n % 2 == 0 or n == 6:
        return 3
    i = 5
    while i * i <= n:
        if n % (i + 1) == 0 or n == i * i:
            return i
        i += 6
    return i + 1
```