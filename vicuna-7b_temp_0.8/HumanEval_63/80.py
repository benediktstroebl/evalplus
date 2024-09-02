

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
    # This implementation uses a sliding window technique to keep track of the sum of the previous two numbers in the sequence.
    # The window size is 3, which means it will keep track of the sum of the previous 3 numbers.
    def fibfib(n: int) -> int:
        if n <= 1:
            return n

        if n in [2, 3]:
            return n

        mid = (n // 2)
        return fibfib(mid) + fibfib(mid - 1)