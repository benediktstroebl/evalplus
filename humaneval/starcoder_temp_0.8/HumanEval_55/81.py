

def fib(n: int):
    """Return n-th Fibonacci number.
    >>> fib(10)
    55
    >>> fib(1)
    1
    >>> fib(8)
    21
    """
    i: int = 0
    j: int = 1
    for _ in range(n-1):
        i, j = j, i+j
    return i
