

def fib(n: int):
    """Return n-th Fibonacci number.
    >>> fib(10)
    55
    >>> fib(1)
    1
    >>> fib(8)
    21
    """

    # fib: int -> int
    # computes the n-th Fibonacci number
    return _fib(n, 1, 0)

