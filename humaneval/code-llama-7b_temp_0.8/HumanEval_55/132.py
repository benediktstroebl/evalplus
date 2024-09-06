

def fib(n: int):
    """Return n-th Fibonacci number.
    >>> fib(10)
    55
    >>> fib(1)
    1
    >>> fib(8)
    21
    """
    if n < 0:
        raise ValueError('n must be nonnegative')
    if n in (0, 1):  # Shortcut
        return n

    before_last = 0
    last = 1
    current = before_last + last
    for _ in range(n - 2):
        before_last = last
        last = current
        current = before_last + last

    return current

