

def fib(n: int):
    """Return n-th Fibonacci number.
    >>> fib(10)
    55
    >>> fib(1)
    1
    >>> fib(8)
    21
    """
    if n == 0:
        return 0
    if n < 0:
        raise ValueError("Fibonacci number is not defined for negative numbers")
    if n == 1:
        return 1
    previous = 0
    current = 1
    sum = 0
    for i in range(1, n):
        sum = previous + current
        previous = current
        current = sum
    return sum
