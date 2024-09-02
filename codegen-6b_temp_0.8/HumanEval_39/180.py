

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
    if n < 1:
        raise ValueError('n must be > 0')
    if n < 3:
        return 2
    a, b = 2, 3
    fib = 0 + 1
    while fib < n:
        fib = a + b
        a, b = b, fib
    return fib
