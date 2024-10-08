

def fib(n: int):
    """Return n-th Fibonacci number.
    >>> fib(10)
    55
    >>> fib(1)
    1
    >>> fib(8)
    21
    """
    if n < 2:
        return 1
    n1, n2 = 1, 1
    for i in range(n - 1):
        n1, n2 = n2, n1 + n2
    return n2

