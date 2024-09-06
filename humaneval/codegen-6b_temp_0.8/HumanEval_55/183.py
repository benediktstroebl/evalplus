

def fib(n: int):
    """Return n-th Fibonacci number.
    >>> fib(10)
    55
    >>> fib(1)
    1
    >>> fib(8)
    21
    """
    if n < 2:
        return 1
    last_two = [None, None]
    for _ in range(n - 1):
        last_two[0], last_two[1] = last_two[1], last_two[0] + last_two[1]
    return last_two[1]
