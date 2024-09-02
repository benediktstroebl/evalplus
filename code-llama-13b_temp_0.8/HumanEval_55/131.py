

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

    assert n >= 1

    def inner_fib(n: int):
        if n <= 2:
            return 1
        else:
            return inner_fib(n - 1) + inner_fib(n - 2)
    return inner_fib(n)



