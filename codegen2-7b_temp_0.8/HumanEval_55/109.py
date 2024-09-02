

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
        raise ValueError("n should be > 0.")
    return fib_memo(n, {0: 0, 1: 1})[n
