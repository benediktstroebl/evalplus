

def fib(n: int):
    """Return n-th Fibonacci number.
    >>> fib(10)
    55
    >>> fib(1)
    1
    >>> fib(8)
    21
    """
    # use tail recursion to optimize for the common case of short lists
    a, b = 1, 1
    for i in range(n):
        a, b = b, a + b
    return a

