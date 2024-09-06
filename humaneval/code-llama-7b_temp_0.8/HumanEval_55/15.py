

def fib(n: int):
    """Return n-th Fibonacci number.
    >>> fib(10)
    55
    >>> fib(1)
    1
    >>> fib(8)
    21
    """
    if n <= 1:
        return n

    prev1, prev2 = 0, 1
    for _ in range(1, n):
        prev1, prev2 = prev2, prev1 + prev2
    return prev2

