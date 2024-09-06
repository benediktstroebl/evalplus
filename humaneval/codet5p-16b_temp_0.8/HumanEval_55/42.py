

def fib(n: int):
    """Return n-th Fibonacci number.
    >>> fib(10)
    55
    >>> fib(1)
    1
    >>> fib(8)
    21
    """

    fib_array = [0, 1]
    for _ in range(n):
        fib_array.append(fib_array[-1] + fib_array[-2])
    return fib_array[n]

