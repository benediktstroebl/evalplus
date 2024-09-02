

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
    c1, c2 = 1, 1
    fib = 1
    while fib < n:
        fib = c1 + c2
        c1, c2 = c2, fib
    if fib == n:
        return fib
    else:
        return fib + 1
