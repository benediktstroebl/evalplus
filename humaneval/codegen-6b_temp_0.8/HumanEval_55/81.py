

def fib(n: int):
    """Return n-th Fibonacci number.
    >>> fib(10)
    55
    >>> fib(1)
    1
    >>> fib(8)
    21
    """
    if n == 1 or n == 0:
        return 1
    last_n_1 = 1
    last_n_2 = 0
    for i in range(n-1):
        last_n_2, last_n_1 = last_n_1, last_n_2 + last_n_1
    return last_n_1

