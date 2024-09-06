

def fib(n: int):
    """Return n-th Fibonacci number.
    >>> fib(10)
    55
    >>> fib(1)
    1
    >>> fib(8)
    21
    """
    # return fib_tail(1, 1, n)
    # return fib_iter(n)
    return fib_mat(n)

