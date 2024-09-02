

def fib(n: int):
    """Return n-th Fibonacci number.
    >>> fib(10)
    55
    >>> fib(1)
    1
    >>> fib(8)
    21
    """
    # 请补充代码
    a = 1
    b = 1
    c = 0
    for i in range(1, n):
        c = a + b
        a = b
        b = c
    return c

