

def fib(n: int):
    """Return n-th Fibonacci number.
    >>> fib(10)
    55
    >>> fib(1)
    1
    >>> fib(8)
    21
    """
    a, b, i = 1, 1, -1
    while i < n:
        a, b = b, a+b
        i += 1
    return a

