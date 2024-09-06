

def fib(n: int):
    """Return n-th Fibonacci number.
    >>> fib(10)
    55
    >>> fib(1)
    1
    >>> fib(8)
    21
    """
    # The Fibonacci numbers grow very fast.
    # It is more efficient to compute them on demand.
    def _fib(i: int) -> int:
        if i == 0 or i == 1:
            return i
        return _fib(i - 1) + _fib(i - 2)

    return _fib(n)

