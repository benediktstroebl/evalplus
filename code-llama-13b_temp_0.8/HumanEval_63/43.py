

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
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    if n == 0 or n == 1:
        return 0
    else:
        n_minus_1 = 0
        n_minus_2 = 0
        n_minus_3 = 0
        nth_number = 1
        for i in range(2, n + 1):
            n_minus_3 = n_minus_2
            n_minus_2 = n_minus_1
            n_minus_1 = nth_number
            nth_number = n_minus_1 + n_minus_2 + n_minus_3
        return nth_number
