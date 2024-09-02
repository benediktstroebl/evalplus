

def fib(n: int):
    """Return n-th Fibonacci number.
    >>> fib(10)
    55
    >>> fib(1)
    1
    >>> fib(8)
    21
    """
    assert n >= 1

    def fib_helper(n: int) -> int:
        if n <= 2:
            return 1
        else:
            return fib_helper(n-1) + fib_helper(n-2)

    return fib_helper(n)


