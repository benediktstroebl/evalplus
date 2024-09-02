

def fib(n: int):
    """Return n-th Fibonacci number.
    >>> fib(10)
    55
    >>> fib(1)
    1
    >>> fib(8)
    21
    """
    # fib(n) = fib(n-1) + fib(n-2)
    if n <= 2:
        return 1
    return fib(n-1) + fib(n-2)
