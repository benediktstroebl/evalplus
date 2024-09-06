

def fib(n: int):
    """Return n-th Fibonacci number.
    >>> fib(10)
    55
    >>> fib(1)
    1
    >>> fib(8)
    21
    """
    if n < 3:
        return 1

    num1 = 1
    num2 = 1
    num3 = 2

    for _ in range(2, n - 1):
        num1 = num2
        num2 = num3
        num3 = num1 + num2

    return num3

