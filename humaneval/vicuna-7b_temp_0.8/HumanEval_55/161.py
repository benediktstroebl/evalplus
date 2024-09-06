

def fib(n: int):
    """Return n-th Fibonacci number.
    >>> fib(10)
    55
    >>> fib(1)
    1
    >>> fib(8)
    21
    """
    a, b = 0, 1
    result = a
    for i in range(n):
        result = b
        b = a + b
        a = result
    return result