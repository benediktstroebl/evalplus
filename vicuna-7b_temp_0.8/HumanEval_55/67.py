

def fib(n: int):
    """Return n-th Fibonacci number.
    >>> fib(10)
    55
    >>> fib(1)
    1
    >>> fib(8)
    21
    """
    a, b = 0, 1
    result = 0
    while b < n:
        result, a, b = b, b + a
    return result

print(fib(15))  # fib(15) = 77