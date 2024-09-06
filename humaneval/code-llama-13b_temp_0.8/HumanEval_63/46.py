

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
    # Submitted by @Jrafahi on LeetCode: https://leetcode.com/problems/fibonacci-number/discuss/646494/Python-oror-DP-oror-Space-O(1)-oror-Time-O(log(n))
    if n < 3:
        return n - 1
    fib2, fib1, fib0 = 1, 1, 0
    while n > 2:
        fib2, fib1, fib0 = fib1 + 2 * fib2, fib2, fib1
        n -= 1
    return fib0 + fib1

