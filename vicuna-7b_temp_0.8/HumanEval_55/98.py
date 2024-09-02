

def fib(n: int):
    """Return n-th Fibonacci number.
    >>> fib(10)
    55
    >>> fib(1)
    1
    >>> fib(8)
    21
    """
    if n <= 1:
        return n, n+1, None
    if n in [2, 3]:
        return n, n+1, fib(n-1) + fib(n-2)
    else:
        return fib(n-1), fib(n-2), fib(n-3)
