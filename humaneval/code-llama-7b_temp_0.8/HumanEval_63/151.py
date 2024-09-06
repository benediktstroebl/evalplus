

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
    # if n <= 2: return n - 1
    # return fibfib(n - 1) + fibfib(n - 2) + fibfib(n - 3)
    if n < 2:
        return n
    f_1, f_2, f_3 = 0, 0, 1
    for _ in range(n - 2):
        f_1, f_2, f_3 = f_2, f_3, f_1 + f_2 + f_3
    return f_1 + f_2 + f_3

