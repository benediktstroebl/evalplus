

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
    if n <= 2:
        return n - 1

    prev2 = 0
    prev1 = 1
    fibfib_n = 1
    for _ in range(3, n + 1):
        tmp = fibfib_n
        fibfib_n += prev1 + prev2
        prev2 = prev1
        prev1 = tmp

    return fibfib_n

