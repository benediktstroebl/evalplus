

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

    def fib(n):
        if n == 0: return 0
        if n == 1: return 1
        return fib(n-1) + fib(n-2)
    return fib(n)


