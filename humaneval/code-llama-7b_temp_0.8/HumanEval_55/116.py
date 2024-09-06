

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
    if n == 0:
        return 0
    for i in range(1, n):
        a, b = b, a + b
    return b

