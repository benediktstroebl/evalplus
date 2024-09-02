

def fib(n: int):
    """Return n-th Fibonacci number.
    >>> fib(10)
    55
    >>> fib(1)
    1
    >>> fib(8)
    21
    """

    fib_numbers = [0, 1]
    if n <= 1:
        return n
    for _ in range(1, n):
        fib_numbers[0], fib_numbers[1] = fib_numbers[1], fib_numbers[0] + fib_numbers[1]
    return fib_numbers[1]
