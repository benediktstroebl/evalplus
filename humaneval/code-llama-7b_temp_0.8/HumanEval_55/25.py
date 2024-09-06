

def fib(n: int):
    """Return n-th Fibonacci number.
    >>> fib(10)
    55
    >>> fib(1)
    1
    >>> fib(8)
    21
    """
    # return 1 if n == 1 else fib(n - 1) + fib(n - 2)
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a
