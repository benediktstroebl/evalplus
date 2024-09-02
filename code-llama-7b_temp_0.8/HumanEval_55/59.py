

def fib(n: int):
    """Return n-th Fibonacci number.
    >>> fib(10)
    55
    >>> fib(1)
    1
    >>> fib(8)
    21
    """
    if n < 1:
        return n
    if n <= 3:
        return 1

    previous = 1
    current = 1
    for i in range(2, n):
        current, previous = current + previous, current

    return current

