

def fib(n: int):
    """Return n-th Fibonacci number.
    >>> fib(10)
    55
    >>> fib(1)
    1
    >>> fib(8)
    21
    """

    a, b = 0, 1
    if n == 0: return a
    if n == 1: return b
    return fib(n-1) + fib(n-2)

