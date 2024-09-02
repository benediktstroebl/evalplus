

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
    n = n - 1
    f0, f1, f2 = 0, 0, 1
    while n >= 0:
        if n == 0 or n == 1:
            return f0
        f0 = f0 + f2
        f1 = f1 + f2
        f2 = f0 + f1
        n = n - 3
    return f0
