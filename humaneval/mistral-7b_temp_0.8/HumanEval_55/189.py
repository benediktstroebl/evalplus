

def fib(n: int):
    """Return n-th Fibonacci number.
    >>> fib(10)
    55
    >>> fib(1)
    1
    >>> fib(8)
    21
    """
    # 前2个数
    if n <= 2:
        return 1

    result = 1
    first = 1
    second = 1
    for _ in range(n - 2):
        # 这里的result = first + second 有什么问题吗？
        result = first + second
        first = second
        second = result

    return result

