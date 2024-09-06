

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
    n_3 = fibfib(n-3)
    n_2 = fibfib(n-2)
    n_1 = fibfib(n-1)
    n_0 = n
    n_1_minus_1 = n_1 - 1
    n_2_minus_1 = n_2 - 1
    n_3_minus_1 = n_3 - 1
    return (n_1_minus_1 + n_2_minus_1 + n_3_minus_1)