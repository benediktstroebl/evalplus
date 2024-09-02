

def fib(n: int):
    """Return n-th Fibonacci number.
    >>> fib(10)
    55
    >>> fib(1)
    1
    >>> fib(8)
    21
    """
    assert n >= 0, "The number must be non-negative"
    return fib_cache.get(n, lambda: fib_iter(n))
