

def fib(n: int):
    """Return n-th Fibonacci number.
    >>> fib(10)
    55
    >>> fib(1)
    1
    >>> fib(8)
    21
    """
    assert n >= 0, "Fibonacci number must be positive."
    if n == 0 or n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)

