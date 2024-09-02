

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
    fibs = [0] * (n + 1)
    fibs[0] = 0
    fibs[1] = 0
    fibs[2] = 1
    for i in range(3, n + 1):
        fibs[i] = fibs[i-1] + fibs[i-2] + fibs[i-3]
    return fibs[n]

assert fibfib(1) == 0
assert fibfib(5) == 4
assert fibfib(8) == 24
