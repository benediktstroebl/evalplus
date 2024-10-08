

def fib(n: int):
    """Return n-th Fibonacci number.
    >>> fib(10)
    55
    >>> fib(1)
    1
    >>> fib(8)
    21
    """
    a = 1
    b = 1
    for i in range(1, n):
        a, b = b, a + b
    return a

