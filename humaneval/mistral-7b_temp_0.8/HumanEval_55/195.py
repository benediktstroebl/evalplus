

def fib(n: int):
    """Return n-th Fibonacci number.
    >>> fib(10)
    55
    >>> fib(1)
    1
    >>> fib(8)
    21
    """

    # Write your code here.
    first = 0
    second = 1
    fib_list = []

    for i in range(2, n + 1):
        fib_list.append(first + second)
        first, second = second, first + second
    return fib_list[-1]

