

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
        return None

    if n == 1:
        return 1
    elif n == 2:
        return 2

    else:
        return fib(n - 1) + fib(n - 2)
