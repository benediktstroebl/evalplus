

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
    memo = {0: 0, 1: 0}

    def fibfib_helper(n: int) -> int:
        if n in memo:
            return memo[n]

        fib_n_minus_1 = fibfib_helper(n-1)
        fib_n_minus_2 = fibfib_helper(n-2)
        fib_n_minus_3 = fibfib_helper(n-3)

        memo[n] = fib_n_minus_1 + fib_n_minus_2 + fib_n_minus_3
        return memo[n]

    return fibfib_helper(n)

