

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
    f, n = 0, n
    while f < n:
        if f % 2 == 0:
            f = 2 * f + 1
        else:
            n = n + 1
        f = 2 * f + 1
    return f