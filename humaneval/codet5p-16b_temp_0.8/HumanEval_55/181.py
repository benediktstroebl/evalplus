

def fib(n: int):
    """Return n-th Fibonacci number.
    >>> fib(10)
    55
    >>> fib(1)
    1
    >>> fib(8)
    21
    """

    assert n > 0, "n > 0 required"
    a, b = 1, 1
    for i in range(n-1):
        a, b = b, a + b
    return b
