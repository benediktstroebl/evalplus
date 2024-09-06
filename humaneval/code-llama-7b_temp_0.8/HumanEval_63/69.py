

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

    def fibfib_recur(n: int):
        """
        Time Complexity: O(2^n)
        """

        if n <= 2:
            return n

        return fibfib_recur(n - 1) + fibfib_recur(n - 2) + fibfib_recur(n - 3)

    def fibfib_dp(n: int):
        """
        Time Complexity: O(n)
        """
        if n <= 2:
            return n

        memo = [0 for i in range(n + 1)]
        memo[0] = 0
        memo[1] = 0
        memo[2] = 1

        for i in range(3, n + 1):
            memo[i] = memo[i - 1] + memo[i - 2] + memo[i - 3]

        return memo[n]

    def fibfib_memo(n: int):
        """
        Time Complexity: O(n)
        """
        memo = [0 for i in range(n + 1)]

        def helper(x: int):
            if x == 0:
                return 0
            if x == 1:
                return 0
            if x == 2:
                return 1
            if memo[x] > 0:
                return memo[x]

            memo[x] = helper(x - 1) + helper(x - 2) + helper(x - 3)
            return memo[x]

        return helper(n)

    return fibfib_memo(n)

