

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
    # __________ 递归版 fib 函数
    if n == 1 or n == 2:
        return 1
    return fib(n - 1) + fib(n - 2)
    # __________
    """

    # __________ 循环版 fib 函数
    res = [1, 1]
    for i in range(2, n):
        res.append(res[i-1] + res[i-2])
    return res[n-1]
    # __________

