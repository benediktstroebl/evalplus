

def fib(n: int):
    """Return n-th Fibonacci number.
    >>> fib(10)
    55
    >>> fib(1)
    1
    >>> fib(8)
    21
    """
    global f_1, f_2
    if n == 1:
        return f_1
    elif n == 2:
        return f_2
    else:
        return fib(n-1) + fib(n-2)
