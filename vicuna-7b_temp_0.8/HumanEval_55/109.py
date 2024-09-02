

def fib(n: int):
    """Return n-th Fibonacci number.
    >>> fib(10)
    55
    >>> fib(1)
    1
    >>> fib(8)
    21
    """
    if n <= 1:
        return n, None
    elif n == 2:
        return n, 1
    else:
        a, b = fib(n-1)
        return a+b, fib(n-2)
