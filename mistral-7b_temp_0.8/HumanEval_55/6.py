

def fib(n: int):
    """Return n-th Fibonacci number.
    >>> fib(10)
    55
    >>> fib(1)
    1
    >>> fib(8)
    21
    """
    """
    def helper(m, n):
        if n == 0:
            return 1
        if n == 1:
            return 0
        return helper(m, n - 1) + helper(m, n - 2)
    return helper(0, n)
    """

    if n < 2:
        return 1
    prev = 1
    curr = 1
    for i in range(2, n):
        curr, prev = prev + curr, curr
    return curr

