

def fib(n: int):
    """Return n-th Fibonacci number.
    >>> fib(10)
    55
    >>> fib(1)
    1
    >>> fib(8)
    21
    """
    # Special case for n == 0 or n == 1
    if n == 0 or n == 1:
        return n
    # Recursive call for the rest
    return fib(n-1) + fib(n-2)
