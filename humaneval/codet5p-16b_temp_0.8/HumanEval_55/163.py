

def fib(n: int):
    """Return n-th Fibonacci number.
    >>> fib(10)
    55
    >>> fib(1)
    1
    >>> fib(8)
    21
    """

    result = None
    a, b = 0, 1
    while b < n:
        a, b = b, a + b
    return a
