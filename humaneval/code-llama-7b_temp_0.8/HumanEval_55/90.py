

def fib(n: int):
    """Return n-th Fibonacci number.
    >>> fib(10)
    55
    >>> fib(1)
    1
    >>> fib(8)
    21
    """

    def loop(i: int, last: int, next_: int):
        if i <= 1:
            return next_
        else:
            return loop(i - 1, next_, next_ + last)

    return loop(n, 0, 1)

