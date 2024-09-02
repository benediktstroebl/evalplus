

def fib(n: int):
    """Return n-th Fibonacci number.
    >>> fib(10)
    55
    >>> fib(1)
    1
    >>> fib(8)
    21
    """
    if n < 3:
        return 1

    n_minus_1 = 1
    n_minus_2 = 1

    for i in range(2, n):
        n_minus_2, n_minus_1 = n_minus_1, n_minus_2 + n_minus_1

    return n_minus_1 + n_minus_2

