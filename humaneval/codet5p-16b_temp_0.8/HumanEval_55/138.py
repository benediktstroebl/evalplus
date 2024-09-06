

def fib(n: int):
    """Return n-th Fibonacci number.
    >>> fib(10)
    55
    >>> fib(1)
    1
    >>> fib(8)
    21
    """

    fib_prev = 0
    fib_prev_prev = 1
    for _ in range(2, n + 1):
        fib_prev_prev, fib_prev = fib_prev, fib_prev + fib_prev_prev
    return fib_prev_prev
