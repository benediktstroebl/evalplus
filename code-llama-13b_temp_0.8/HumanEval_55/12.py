

def fib(n: int):
    """Return n-th Fibonacci number.
    >>> fib(10)
    55
    >>> fib(1)
    1
    >>> fib(8)
    21
    """
    # no need to use recursion, but here it is.
    return n if n <= 2 else fib(n-1) + fib(n-2)

