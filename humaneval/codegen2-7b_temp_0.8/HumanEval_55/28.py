

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
        raise ValueError("Argument n should be a positive integer")
    return fib_rec(n - 1) + fib_rec(n - 2)

