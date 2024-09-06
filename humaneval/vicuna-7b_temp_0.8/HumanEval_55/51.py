

def fib(n: int):
    """Return n-th Fibonacci number.
    >>> fib(10)
    55
    >>> fib(1)
    1
    >>> fib(8)
    21
    """
    # 0 and 1 are not Fibonacci numbers.
    if n < 2:
        return n, 1
    # Calculate previous two numbers.
    a, b = 0, 1
    for i in range(n-1):
        a, b = b, a + b
    return a, b
