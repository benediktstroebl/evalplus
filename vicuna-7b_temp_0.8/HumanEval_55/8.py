

def fib(n: int):
    """Return n-th Fibonacci number.
    >>> fib(10)
    55
    >>> fib(1)
    1
    >>> fib(8)
    21
    """
    # Starting values for current and previous numbers
    a, b = 0, 1

    # Loop through numbers until we reach the desired value
    for i in range(n):
        yield a
        a, b = b, a + b
