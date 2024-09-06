

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
    if n < 2:
        return 0
    elif n == 2:
        return 1
    elif n < 5:
        return 1
    elif n % 5 == 0:
        return fibfib(n - 1) + fibfib(n - 2) + fibfib(n - 3) + fibfib(n - 4) + fibfib(n - 5)
    else:
        return fibfib(n - 1) + fibfib(n - 2) + fibfib(n - 3) + fibfib(n - 4) + fibfib(n - 5) + fibfib(n - 6) + fibfib(n - 7) + fibfib(n - 8) + fibfib(n - 9) + fibfib(n - 10) + fibfib(n - 11) + fibfib(n - 12) + fibfib(n - 13) + fibfib(n - 14) + fibfib(n - 15) + fibfib(n - 16) + fibfib(n - 17) + fibfib(n - 18) + fibfib(n - 19) + fibfib(n - 20) + fibfib(n - 21) + fibfib(n - 22) + fibfib(n - 23) + fibfib(n - 24) + fibfib(n - 25) + fibfib(n - 26) + fibfib(n - 27) + fibfib(n - 28) + fibfib(n - 29) + fibfib(n - 30)
