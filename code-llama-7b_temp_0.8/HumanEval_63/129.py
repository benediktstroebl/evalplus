

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
    # fibfib(3) = fibfib(2) + fibfib(1) + fibfib(0) = 1
    # fibfib(4) = fibfib(3) + fibfib(2) + fibfib(1) = 1 + 1 + 0 = 2
    # fibfib(5) = fibfib(4) + fibfib(3) + fibfib(2) = 2 + 1 + 1 = 4
    # fibfib(6) = fibfib(5) + fibfib(4) + fibfib(3) = 4 + 2 + 1 = 7
    if n == 0 or n == 1:
        return n

    # fibfib(2) = 1
    prev = 1
    # fibfib(3) = 1
    prev_prev = 1
    # fibfib(4) = 1
    prev_prev_prev = 1
    i = 4
    while i <= n:
        curr = prev + prev_prev + prev_prev_prev
        prev_prev_prev = prev_prev
        prev_prev = prev
        prev = curr
        i += 1

    return prev

