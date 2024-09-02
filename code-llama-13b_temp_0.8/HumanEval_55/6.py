

def fib(n: int):
    """Return n-th Fibonacci number.
    >>> fib(10)
    55
    >>> fib(1)
    1
    >>> fib(8)
    21
    """
    if n < 0:
        raise ValueError("n must be >= 0")

    if n <= 1:
        return n

    fib_minus_1 = 1
    fib_minus_2 = 0
    fib_n = 0

    for i in range(2, n+1):
        fib_n = fib_minus_1 + fib_minus_2
        fib_minus_2 = fib_minus_1
        fib_minus_1 = fib_n

    return fib_n

