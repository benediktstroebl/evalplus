

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
        raise ValueError("Fibonacci number can not be less than 1")
    if n < 3:
        return 1
    return fib(n-1) + fib(n-2)
