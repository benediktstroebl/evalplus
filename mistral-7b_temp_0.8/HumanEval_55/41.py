

def fib(n: int):
    """Return n-th Fibonacci number.
    >>> fib(10)
    55
    >>> fib(1)
    1
    >>> fib(8)
    21
    """
    # initial value
    x, y = 1, 1
    for i in range(n - 2):
        x, y = y, x + y
    return y

