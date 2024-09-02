

def fib(n: int):
    """Return n-th Fibonacci number.
    >>> fib(10)
    55
    >>> fib(1)
    1
    >>> fib(8)
    21
    """

    if n == 0:
        return 0

    if n == 1:
        return 1

    prev, cur = 1, 1

    for _ in range(2, n):
        prev, cur = cur, prev + cur

    return cur

