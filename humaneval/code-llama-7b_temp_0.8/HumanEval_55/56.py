

def fib(n: int):
    """Return n-th Fibonacci number.
    >>> fib(10)
    55
    >>> fib(1)
    1
    >>> fib(8)
    21
    """
    if n < 0:
        raise ValueError('Fibonacci numbers are only defined for n >= 0')

    return fib_recur(n)

