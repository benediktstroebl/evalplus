

def fib(n: int):
    """Return n-th Fibonacci number.
    >>> fib(10)
    55
    >>> fib(1)
    1
    >>> fib(8)
    21
    """

    # 0 and 1 are the first two Fibonacci numbers
    if n == 0 or n == 1:
        return n
    else:
        # the rest of the numbers can be found by summing the previous two
        # NOTE: you should assign to fib(n - 1) first and fib(n - 2) second
        #       to avoid repeated work
        n_minus_2 = fib(n - 2)
        n_minus_1 = fib(n - 1)
        return n_minus_2 + n_minus_1

