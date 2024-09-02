

def fib(n: int):
    """Return n-th Fibonacci number.
    >>> fib(10)
    55
    >>> fib(1)
    1
    >>> fib(8)
    21
    """

    assert n >= 0, 'n must be positive integer.'
    if n == 0 or n == 1:
        return 1
    return fib(n-2) + fib(n-1)
