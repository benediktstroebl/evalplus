

def fib(n: int):
    """Return n-th Fibonacci number.
    >>> fib(10)
    55
    >>> fib(1)
    1
    >>> fib(8)
    21
    """
    assert n >= 0
    return fib(n - 1) + fib(n - 2) if n > 1 else n
