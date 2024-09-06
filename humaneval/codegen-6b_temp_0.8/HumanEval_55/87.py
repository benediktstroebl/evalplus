

def fib(n: int):
    """Return n-th Fibonacci number.
    >>> fib(10)
    55
    >>> fib(1)
    1
    >>> fib(8)
    21
    """
    global accumulator
    accumulator = 1
    if n <= 0:
        return accumulator
    fib(n - 1)
    accumulator += accumulator
    return accumulator

