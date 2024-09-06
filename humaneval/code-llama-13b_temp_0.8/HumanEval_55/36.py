

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
    def fib_helper(n: int):
        if n == 1 or n == 2:
            return 1
        return fib_helper(n - 1) + fib_helper(n - 2)
    return fib_helper(n)

