

def fib(n: int):
    """Return n-th Fibonacci number.
    >>> fib(10)
    55
    >>> fib(1)
    1
    >>> fib(8)
    21
    """

    f1, f2 = 0, 1
    for i in range(n):
        f1, f2 = f2, f1 + f2
    return f1
