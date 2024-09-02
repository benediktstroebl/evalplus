

def fib(n: int):
    """Return n-th Fibonacci number.
    >>> fib(10)
    55
    >>> fib(1)
    1
    >>> fib(8)
    21
    """

    if n < 0:
        raise ValueError("incorrect input")
    f0, f1 = 0, 1
    for i in range(n):
        f0, f1 = f1, f0 + f1
    return f0

