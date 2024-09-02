

def fib(n: int):
    """Return n-th Fibonacci number.
    >>> fib(10)
    55
    >>> fib(1)
    1
    >>> fib(8)
    21
    """
    if n < 1:
        raise ValueError("n must be >= 1")

    i = 0
    j = 1
    for _ in range(n-1):
        i, j = j, i+j
    return j
