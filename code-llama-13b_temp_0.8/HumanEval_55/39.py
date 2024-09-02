

def fib(n: int):
    """Return n-th Fibonacci number.
    >>> fib(10)
    55
    >>> fib(1)
    1
    >>> fib(8)
    21
    """
    "*** YOUR CODE HERE ***"
    def helper(n: int):
        if n == 0:
            return 1, 0
        else:
            a, b = helper(n//2)
            c = a * (2 * b - a)
            d = a * a + b * b
            if n % 2 == 0:
                return c, d
            else:
                return d, c + d
        return helper(n)[0]
    return helper(n - 1)
