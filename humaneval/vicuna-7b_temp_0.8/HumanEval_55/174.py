

def fib(n: int):
    """Return n-th Fibonacci number.
    >>> fib(10)
    55
    >>> fib(1)
    1
    >>> fib(8)
    21
    """
    # fibonacci sequence has only two numbers
    if n < 0 or n > 1:
        raise ValueError("Invalid input")

    # compute nth number in sequence
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b

    return a
