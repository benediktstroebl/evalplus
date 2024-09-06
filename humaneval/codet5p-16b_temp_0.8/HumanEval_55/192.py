

def fib(n: int):
    """Return n-th Fibonacci number.
    >>> fib(10)
    55
    >>> fib(1)
    1
    >>> fib(8)
    21
    """

    fib1 = 1
    fib2 = 1
    if n == 1:
        return fib1
    elif n == 2:
        return fib2
    for i in range(2, n):
        temp = fib2
        fib2 = fib2 + fib1
        fib1 = temp
    return fib2
