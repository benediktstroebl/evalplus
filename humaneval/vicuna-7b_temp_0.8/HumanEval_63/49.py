

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
    # If n is 0 or 1, return 0 or 1 respectively.
    if n <= 1:
        return n
    # A helper variable to store the running sum.
    running_sum = fibfib(n-1) + fibfib(n-2) + fibfib(n-3)
    # Return the n-th element of the sequence.
    return running_sum