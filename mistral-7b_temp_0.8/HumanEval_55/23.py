

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
    for i in range(n - 2):
        c = a + b
        a = b
        b = c
    return a

