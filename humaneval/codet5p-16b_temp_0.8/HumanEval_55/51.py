

def fib(n: int):
    """Return n-th Fibonacci number.
    >>> fib(10)
    55
    >>> fib(1)
    1
    >>> fib(8)
    21
    """

    assert n > 0, "n must be positive"

    if n == 1 or n == 2:
        return 1
    return fib(n - 1) + fib(n - 2)
