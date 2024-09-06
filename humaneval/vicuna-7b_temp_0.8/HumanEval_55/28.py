

def fib(n: int):
    """Return n-th Fibonacci number.
    >>> fib(10)
    55
    >>> fib(1)
    1
    >>> fib(8)
    21
    """
    # n is 0 or 1, so the answer is 0 or 1
    if n <= 1:
        return n
    # n is 2 or greater, so we can use recursion
    return fib(n-1) + fib(n-2)
