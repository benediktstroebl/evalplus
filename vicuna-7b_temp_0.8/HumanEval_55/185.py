

def fib(n: int):
    """Return n-th Fibonacci number.
    >>> fib(10)
    55
    >>> fib(1)
    1
    >>> fib(8)
    21
    """
    # fibonacci sequence
    a, b = 0, 1
    result = a
    for i in range(n):
        result = b + result
        b, a = a, b + result
    return result
