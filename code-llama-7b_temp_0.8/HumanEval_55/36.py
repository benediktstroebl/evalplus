

def fib(n: int):
    """Return n-th Fibonacci number.
    >>> fib(10)
    55
    >>> fib(1)
    1
    >>> fib(8)
    21
    """
    # Source: https://www.geeksforgeeks.org/program-for-fibonacci-numbers/
    a = 0
    b = 1
    if n < 1:
        return n
    if n == 1:
        return a
    if n == 2:
        return b
    for i in range(3, n + 1):
        c = a + b
        a = b
        b = c
    return b
