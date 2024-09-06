

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
    # 1 1 1 2 2 3 3 4 4 5 5 6 6 7 7 8 8 9 9 10 10 11 11 12 12 13 13 14 14 15 15 16 16 17 17 18 18 19 19 20 20 21 21
    # 11 13 13 15 15 17 17 19 19 21 21 23 23 25 25 25 27 27 29 29 31 31 33 33 35 35 37 37 39 39 41 41 43 43 45 45 47 47
    # 6 6 8 8 10 10 12 12 14 14 16 16 18 18 20 20 22 22 24 24 26 26 28 28 30 30 32 32 34 34 36 36 38 38 40 40 42 42 44 44
    # 5 5 7 7 9 9 11 11 13 13 15 15 17 17 19 19 21 21 23 23 25 25 27 27 29 29 31 31 33 33 35 35 37 37 39 39 41 41 43 43
    # 6 6 7 7 9 9 11 11 13 13 15 15 17 17 19 19 2
