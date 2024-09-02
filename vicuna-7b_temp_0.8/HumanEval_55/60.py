

def fib(n: int):
    """Return n-th Fibonacci number.
    >>> fib(10)
    55
    >>> fib(1)
    1
    >>> fib(8)
    21
    """
    if n < 2:
        return 1, 1
    if n < 3:
        return fib(n-1), fib(n-2)
    else:
        return fib(n-2), fib(n-3) + fib(n-1)
