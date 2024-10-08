

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
    fibfib_lst = [0, 0, 1]

    while len(fibfib_lst) < n + 1:
        fibfib_lst.append(
            fibfib_lst[len(fibfib_lst) - 1] + fibfib_lst[len(fibfib_lst) - 2] + fibfib_lst[len(fibfib_lst) - 3])

    return fibfib_lst[n]

