

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

    def fibfib_rec(n: int, fibfib_n_2: int = 0, fibfib_n_1: int = 0, fibfib_n: int = 0):
        if n == 0:
            return fibfib_n_2
        if n == 1:
            return fibfib_n_1
        if n == 2:
            return fibfib_n
        else:
            return fibfib_rec(n - 1, fibfib_n_1, fibfib_n, fibfib_n_2 + fibfib_n_1 + fibfib_n)

    return fibfib_rec(n)

