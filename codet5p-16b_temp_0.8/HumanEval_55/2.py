

def fib(n: int):
    """Return n-th Fibonacci number.
    >>> fib(10)
    55
    >>> fib(1)
    1
    >>> fib(8)
    21
    """

    n1, n2 = 0, 1
    for _ in range(n):
        n1, n2 = n2, n1+n2
    return n2

