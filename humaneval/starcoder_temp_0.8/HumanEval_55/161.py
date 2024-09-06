

def fib(n: int):
    """Return n-th Fibonacci number.
    >>> fib(10)
    55
    >>> fib(1)
    1
    >>> fib(8)
    21
    """
    i = 1
    a = 0
    b = 1
    while i < n:
        c = a + b
        a = b
        b = c
        i += 1
    return b
