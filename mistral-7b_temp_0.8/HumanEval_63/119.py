

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
    fibfib_0 = 0
    fibfib_1 = 0
    fibfib_2 = 1
    if n == 0 or n == 1:
        return fibfib_0
    if n == 2:
        return fibfib_2
    fibfib_n = fibfib_n - 1 + fibfib_n - 2 + fibfib_n - 3
    return fibfib_n

