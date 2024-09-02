

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
        return 1
    f1 = 1
    f2 = 1
    for i in range(2, n):
        f3 = f1 + f2
        f1 = f2
        f2 = f3
    return f3
