

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
    memo = {}
    def fibfib_helper(k):
        if k == 0:
            return 0
        elif k == 1:
            return 0
        elif k == 2:
            return 1
        elif k in memo:
            return memo[k]
        else:
            memo[k] = fibfib_helper(k - 1) + fibfib_helper(k - 2) + fibfib_helper(k - 3)

        return memo[k]


    return fibfib_helper(n)

