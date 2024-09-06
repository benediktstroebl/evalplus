

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
    # The function uses a sliding window approach to compute the fibfib number.
    # The sliding window approach reduces the number of times we need to add two numbers together.
    # We use a max window size of 5, which means that we'll compute up to the 5th number in the sequence.
    n_1, n_2, n_3 = n - 1, n - 2, n - 3
    result = n_1 + n_2 + n_3
    while result <= n:
        result = n_1 + n_2 + n_3
        n_1, n_2, n_3 = n_1, n_2 - 1, n_3 - 1
    return result
