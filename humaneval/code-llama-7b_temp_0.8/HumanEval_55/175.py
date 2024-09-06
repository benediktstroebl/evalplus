

def fib(n: int):
    """Return n-th Fibonacci number.
    >>> fib(10)
    55
    >>> fib(1)
    1
    >>> fib(8)
    21
    """
    # Ensure we only use integer division.
    return n if n <= 1 else fib(n - 1) + fib(n - 2)
