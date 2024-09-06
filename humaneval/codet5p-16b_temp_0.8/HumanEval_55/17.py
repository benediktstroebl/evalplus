

def fib(n: int):
    """Return n-th Fibonacci number.
    >>> fib(10)
    55
    >>> fib(1)
    1
    >>> fib(8)
    21
    """

    f_2 = 0
    f_1 = 1
    for i in range(n):
        f = f_1 + f_2
        f_2 = f_1
        f_1 = f
    return f
