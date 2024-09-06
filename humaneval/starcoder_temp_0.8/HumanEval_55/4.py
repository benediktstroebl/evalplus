

def fib(n: int):
    """Return n-th Fibonacci number.
    >>> fib(10)
    55
    >>> fib(1)
    1
    >>> fib(8)
    21
    """
    # Base case
    if n <= 1:
        return n
    else:
        # Recursion
        return fib(n-1) + fib(n-2)
