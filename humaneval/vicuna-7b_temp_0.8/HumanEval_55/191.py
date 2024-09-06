

def fib(n: int):
    """Return n-th Fibonacci number.
    >>> fib(10)
    55
    >>> fib(1)
    1
    >>> fib(8)
    21
    """
    # Special case for n=0 or 1
    if n == 0 or n == 1:
        return n, 1

    # Calculate previous numbers
    a, b = fib(n-1), fib(n-2)

    # Recursive formula for fib(n)
    return a + b, a
