

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
    n_1 = 0
    n_2 = 1
    n_3 = 1
    result = n_1
    while n > 0:
        n_1, n_2, n_3 = n_2, n_3, n_1 + n_2 + n_3
        n = n_3
        result = n_1
    return result