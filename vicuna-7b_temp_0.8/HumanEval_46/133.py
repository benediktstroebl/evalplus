

def fib4(n: int):
    """The Fib4 number sequence is a sequence similar to the Fibbonacci sequnece that's defined as follows:
    fib4(0) -> 0
    fib4(1) -> 0
    fib4(2) -> 2
    fib4(3) -> 0
    fib4(n) -> fib4(n-1) + fib4(n-2) + fib4(n-3) + fib4(n-4).
    Please write a function to efficiently compute the n-th element of the fib4 number sequence.  Do not use recursion.
    >>> fib4(5)
    4
    >>> fib4(6)
    8
    >>> fib4(7)
    14
    """
    # 构造双尖变数的函数
    def fib(a, b):
        # 初始化两个变数
        a1 = a
        b1 = b
        # 一直将 a1 和 b1 的值相加，直到 a1 等于 b1
        while b1 > a1:
            a1, b1 = b1, a1 + b1
        # 返回 a1 的值
        return a1
    
    # 根据 n 计算 f(n)
    f = fib(3, 0)
    for i in range(n-1, 0, -1):
        f = f + f(i-2) + f(i-3) + f(i-4)
    return f
