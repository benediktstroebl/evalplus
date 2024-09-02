

def fib(n: int):
    """Return n-th Fibonacci number.
    >>> fib(10)
    55
    >>> fib(1)
    1
    >>> fib(8)
    21
    """

    result = 0
    previous = 1
    current = 1
    for i in range(n-1):
        result = current
        current += previous
        previous = result
    return result

