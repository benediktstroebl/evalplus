

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
    # Check if the number is zero, if it is, return 0
    if n <= 0:
        return 0

    # Otherwise, we can use memoization to cache the previous fibonacci numbers
    # and use them to compute the current number.
    # For this example, we'll use a dictionary with the previous numbers as keys and their sum as values.
    memo = {}
    for i in range(n-1):
        memo[i] = fibfib(i)

    return memo[n-1] + memo[n-2] + memo[n-3]