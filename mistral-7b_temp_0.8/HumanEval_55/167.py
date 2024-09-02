

def fib(n: int):
    """Return n-th Fibonacci number.
    >>> fib(10)
    55
    >>> fib(1)
    1
    >>> fib(8)
    21
    """
    # 1 1 2 3 5 8 13 21 34
    if n <= 2:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)

