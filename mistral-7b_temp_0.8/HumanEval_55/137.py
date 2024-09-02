

def fib(n: int):
    """Return n-th Fibonacci number.
    >>> fib(10)
    55
    >>> fib(1)
    1
    >>> fib(8)
    21
    """
    fib_n = 1
    fib_n_1 = 1
    for _ in range(n):
        fib_n_1, fib_n = fib_n, fib_n + fib_n_1
    return fib_n

