

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
        raise ValueError("n must be >= 1")
    if n == 1:
        return 1

    return fib(n - 2) + fib(n - 1)

