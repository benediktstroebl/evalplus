

def fib(n: int):
    """Return n-th Fibonacci number.
    >>> fib(10)
    55
    >>> fib(1)
    1
    >>> fib(8)
    21
    """

    # base cases
    if n in (0, 1):
        return n
    else:
        # recursive calls
        return fib(n-2) + fib(n-1)
