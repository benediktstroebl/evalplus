

def fib(n: int):
    """Return n-th Fibonacci number.
    >>> fib(10)
    55
    >>> fib(1)
    1
    >>> fib(8)
    21
    """

    # Implementing the Fibonacci sequence with a while loop
    a, b = 0, 1
    if n == 0:
        return 0
    if n == 1:
        return 1
    while n > 1:
        a, b = b, a + b
        n -= 1
    return b

