

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
        raise ValueError("n must be greater than 0")
    a, b = 0, 1
    while n > 1:
        a, b = b, a + b
        n -= 1
    return b

