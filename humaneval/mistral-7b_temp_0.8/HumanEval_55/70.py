

def fib(n: int):
    """Return n-th Fibonacci number.
    >>> fib(10)
    55
    >>> fib(1)
    1
    >>> fib(8)
    21
    """
    """
    return 0 if n < 0 else 1 if n < 2 else fib(n - 2) + fib(n - 1)
    """
    if n < 2:
        return n
    else:
        return fib(n - 1) + fib(n - 2)

