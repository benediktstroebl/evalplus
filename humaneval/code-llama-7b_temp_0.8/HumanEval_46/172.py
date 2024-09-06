

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
    f1 = f2 = f3 = f4 = f5 = f6 = 0
    f = [f1, f2, f3, f4, f5, f6]
    for i in range(n+1):
        f[i], f1, f2, f3, f4, f5, f6 = f[i] + f1 + f2 + f3 + f4, f[0], f[1], f[2], f[3], f[4], f[5]
    return f[n]











