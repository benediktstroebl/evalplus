

def fib(n: int):
    """Return n-th Fibonacci number.
    >>> fib(10)
    55
    >>> fib(1)
    1
    >>> fib(8)
    21
    """

    fib_nums = [1, 1]
    while len(fib_nums) < n:
        fib_nums.append(fib_nums[-2] + fib_nums[-1])
    return fib_nums[n-1]

