

def fib(n: int):
    """Return n-th Fibonacci number.
    >>> fib(10)
    55
    >>> fib(1)
    1
    >>> fib(8)
    21
    """

    f_prev, f_curr = 0, 1
    for i in range(n):
        f_prev, f_curr = f_curr, f_curr + f_prev
    return f_prev

