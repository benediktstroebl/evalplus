

def fib(n: int):
    """Return n-th Fibonacci number.
    >>> fib(10)
    55
    >>> fib(1)
    1
    >>> fib(8)
    21
    """
    assert n >= 0, "n must be >= 0"
    # return n if n <= 1 else fib(n-1) + fib(n-2)
    # TODO: use dict to cache computed values?
    if n in [0, 1]:
        return 1
    return fib(n - 1) + fib(n - 2)
