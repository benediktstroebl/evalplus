

def fib(n: int):
    """Return n-th Fibonacci number.
    >>> fib(10)
    55
    >>> fib(1)
    1
    >>> fib(8)
    21
    """
    def fib_recur(n, current, last):
        if n == 0:
            return current
        else:
            return fib_recur(n - 1, current + last, current)

    return fib_recur(n, 1, 0)

