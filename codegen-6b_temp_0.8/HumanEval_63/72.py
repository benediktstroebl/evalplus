

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
    n0 = 0
    n1 = 0
    n2 = 1
    if n == 0:
        return n0
    elif n == 1:
        return n1
    elif n == 2:
        return n2
    else:
        for i in range(3, n + 1):
            nth = n2 + n1 + n0
            n0, n1, n2 = n2, n1, nth
        return nth
