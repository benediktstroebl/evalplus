

def fib(n: int):
    """Return n-th Fibonacci number.
    >>> fib(10)
    55
    >>> fib(1)
    1
    >>> fib(8)
    21
    """
    if n < 1:
        raise ValueError('Argument must be >= 1')
    return fib_helper(n - 1) + fib_helper(n - 2
