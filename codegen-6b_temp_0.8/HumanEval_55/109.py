

def fib(n: int):
    """Return n-th Fibonacci number.
    >>> fib(10)
    55
    >>> fib(1)
    1
    >>> fib(8)
    21
    """
    if n <= 0:
        raise ValueError('n must be > 0')
    return 1 if n <= 1 else fib(n-1) + fib(n-2)

