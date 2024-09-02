

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
    斐波纳契数列：
    1. 当n=1,返回1
    2. 当n=2,返回1
    3. 当n>2,返回前两个数相加
    """
    if n <= 2:
        return 1
    return fib(n - 1) + fib(n - 2)

