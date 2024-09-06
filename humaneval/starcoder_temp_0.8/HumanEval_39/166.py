

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
    from utils import prime
    i = 2
    f = 2
    while i < n:
        f, i = f + i, i + 1
        while not prime(f): f = f + i
    return f
