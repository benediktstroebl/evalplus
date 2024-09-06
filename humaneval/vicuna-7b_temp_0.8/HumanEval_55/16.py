

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
        raise ValueError("n must be non-negative")

    if n == 0:
        return 0
    elif n == 1:
        return 1

    a, b = 0, 1
    result = a

    for i in range(n):
        result = fib(a + b)
        a, b = b, result

    return result