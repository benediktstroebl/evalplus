

def fib(n: int):
    """Return n-th Fibonacci number.
    >>> fib(10)
    55
    >>> fib(1)
    1
    >>> fib(8)
    21
    """
    a, b = 0, 1
    result = 0
    for i in range(n):
        result, a, b = b, a+result, a+b
    return result
