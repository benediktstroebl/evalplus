

def fib(n: int):
    """Return n-th Fibonacci number.
    >>> fib(10)
    55
    >>> fib(1)
    1
    >>> fib(8)
    21
    """

    a = 0
    b = 1
    for i in range(n):
        if a == 0:
            a = 0
            b = 1
        else:
            a, b = b, a + b
    return a

