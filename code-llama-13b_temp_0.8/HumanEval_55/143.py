

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
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        for i in range(n-1):
            a, b = b, a+b
    return b
