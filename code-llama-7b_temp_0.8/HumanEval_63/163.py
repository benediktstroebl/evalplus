

def fibfib(n: int):
    """The FibFib number sequence is a sequence similar to the Fibbonacci sequnece that's defined as follows:
    fibfib(0) == 0
    fibfib(1) == 0
    fibfib(2) == 1
    fibfib(n) == fibfib(n-1) + fibfib(n-2) + fibfib(n-3).
    Please write a function to efficiently compute the n-th element of the fibfib number sequence.
    >>> fibfib(1)
    0
    >>> fibfib(5)
    4
    >>> fibfib(8)
    24
    """
    if n < 4:
        return n - 1
    f2 = 0
    f3 = 0
    f4 = 1
    for i in range(4, n + 1):
        f5 = f2 + f3 + f4
        f2 = f3
        f3 = f4
        f4 = f5
    return f5

