

def fib(n: int):
    """Return n-th Fibonacci number.
    >>> fib(10)
    55
    >>> fib(1)
    1
    >>> fib(8)
    21
    """
    f = 1
    s = 0
    f2 = 1
    s2 = 0
    if n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        for i in range(2, n):
            s, f = f, s + f
            f2, s2 = s2, f2 + s2
        return s + s2

