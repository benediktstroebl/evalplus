

def fib(n: int):
    """Return n-th Fibonacci number.
    >>> fib(10)
    55
    >>> fib(1)
    1
    >>> fib(8)
    21
    """
    prev, curr = 1, 1
    # prev = 1, curr is prev + prev
    for _ in range(n - 1):
        curr, prev = curr + prev, curr
    return curr
