

def prime_fib(n: int):
    """
    prime_fib returns n-th number that is a Fibonacci number and it's also prime.
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
    """
    if n < 2:
        return 2
    if n < 3:
        return 3
    if n % 2 == 0:
        return 1
    d = 1
    for i in range(2, n-1):
        d = (d * i + (n-i-1)) / 2
    return d