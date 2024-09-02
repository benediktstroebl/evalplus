

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
    if n <= 1:
        return n
    fib_seq = [0, 1, 1]
    i = 2
    while i < n:
        fib_seq.append(fib_seq[i - 1] + fib_seq[i - 2] + fib_seq[i - 2])
        i += 1
    return fib_seq[n - 1]
