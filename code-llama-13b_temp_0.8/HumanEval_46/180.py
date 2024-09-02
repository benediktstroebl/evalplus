

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
    if n < 0:
        return 0
    fib_0 = 0
    fib_1 = 0
    fib_2 = 2
    fib_3 = 0
    if n == 0:
        return fib_0
    if n == 1:
        return fib_1
    if n == 2:
        return fib_2
    if n == 3:
        return fib_3
    for i in range(4, n + 1):
        fib = fib_0 + fib_1 + fib_2 + fib_3
        fib_0 = fib_1
        fib_1 = fib_2
        fib_2 = fib_3
        fib_3 = fib
    return fib
