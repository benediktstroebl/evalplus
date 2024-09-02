

def fib(n: int):
    """Return n-th Fibonacci number.
    >>> fib(10)
    55
    >>> fib(1)
    1
    >>> fib(8)
    21
    """
    a, b = 1, 1
    while n > 2:
        a, b = b, a + b
        n -= 1
    return b

