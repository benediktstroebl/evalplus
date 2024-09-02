

def fib(n: int):
    """Return n-th Fibonacci number.
    >>> fib(10)
    55
    >>> fib(1)
    1
    >>> fib(8)
    21
    """
    fib_list = [1, 1]
    for i in range(n-2):
        fib_list.append(fib_list[-1] + fib_list[-2])

    return fib_list[n-1]
