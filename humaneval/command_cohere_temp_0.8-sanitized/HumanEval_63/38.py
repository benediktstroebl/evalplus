from collections import Sequence
def fibfib_seq(n: int, memo: Sequence = None) -> int:
    if n < 0:
        raise ValueError("FibFib sequence is undefined for negative integers")
    
    if n == 0:
        return 0
    if n == 1:
        return 0
    if n == 2:
        return 1
    
    if memo is None:
        memo = [0, 0, 1]
    elif n < len(memo):
        return memo[n]
    
    memo[n] = fibfib_seq(n - 1, memo) + fibfib_seq(n - 2, memo) + fibfib_seq(n - 3, memo)
    return memo[n]
def fibfib(n: int = None) -> int:
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
    if n is not None:
        return fibfib_seq(n)
    
    return fibfib_seq