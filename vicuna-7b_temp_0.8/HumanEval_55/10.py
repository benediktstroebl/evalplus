

def fib(n: int):
    """Return n-th Fibonacci number.
    >>> fib(10)
    55
    >>> fib(1)
    1
    >>> fib(8)
    21
    """
    # Implementation of the recursive fibonacci function.
    # This is one of the simplest possible ways to write a fibonacci function.
    if n <= 1:
        return n
    else:
        return fib(n-1) + fib(n-2)