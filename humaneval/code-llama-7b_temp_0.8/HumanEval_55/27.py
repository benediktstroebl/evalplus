

def fib(n: int):
    """Return n-th Fibonacci number.
    >>> fib(10)
    55
    >>> fib(1)
    1
    >>> fib(8)
    21
    """
    a, b = 1, 1
    while n > 1:
        a, b, n = a+b, a, n-1
    return a

