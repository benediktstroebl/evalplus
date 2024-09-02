

def fib(n: int):
    """Return n-th Fibonacci number.
    >>> fib(10)
    55
    >>> fib(1)
    1
    >>> fib(8)
    21
    """
    a = 1
    b = 1
    if n == 1:
        return a
    elif n == 0:
        return b
    for i in range(2, n):
        c = a + b
        a = b
        b = c
    return b

