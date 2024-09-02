

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
    def fibfib_rec(n):
        return fibfib_rec(n - 1) + fibfib_rec(n - 2) + fibfib_rec(n - 3)

    fibfib_rec.fibfib_memo = {}
    def fibfib_memo(n):
        if n < 0:
            return 0
        if n < 3:
            return n
        if n in fibfib_rec.fibfib_memo:
            return fibfib_rec.fibfib_memo[n]
        res = fibfib_memo(n - 1) + fibfib_memo(n - 2) + fibfib_memo(n - 3)
        fibfib_rec.fibfib_memo[n] = res
        return res

    return fibfib_memo(n)

