

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
        return n, 1
    if n == 2:
        return 1, 1
    if n == 3:
        return 2, 1
    if n == 4:
        return 1, 2
    a, b = 0, 1
    for i in range(n-1, -1, -1):
        a, b = b, a + b
    return a, b
