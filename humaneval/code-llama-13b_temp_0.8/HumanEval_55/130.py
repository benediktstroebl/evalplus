

def fib(n: int):
    """Return n-th Fibonacci number.
    >>> fib(10)
    55
    >>> fib(1)
    1
    >>> fib(8)
    21
    """

    # initial case.
    if n <= 1:
        return n

    # 0,1,1,2,3,5,8,13
    # 3 cases
    # 0,1,2,3

    # recurence relation.
    # f(n) = f(n-1) + f(n-2)

    # fib(4)
    # fib(3) + fib(2)

    # fib(2) + fib(1) + fib(1) + fib(0)

    return fib(n-1) + fib(n-2)

