

def fib(n: int):
    """Return n-th Fibonacci number.
    >>> fib(10)
    55
    >>> fib(1)
    1
    >>> fib(8)
    21
    """
    if n <= 0:
        return 0, 1

    if n == 1:
        return 1, 1

    a, b = 0, 1
    result = a
    for i in range(n-1):
        a, b = b, a + b
        result = a + b

    return result, a
