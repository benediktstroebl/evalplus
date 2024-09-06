

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
    def calc(n):
        if n < 1:
            return 0
        elif n == 1:
            return 0
        elif n == 2:
            return 1
        elif n == 3:
            return 1
        else:
            return calc(n-1) + calc(n-2) + calc(n-3)

    return calc(n)

