from typing import Optional
def fibfib_naive(n: int, memo: Optional[dict] = None) -> int:
    if n < 0:
        raise ValueError("FibFib is only defined for non-negative integers.")
    
    if memo is None:
        memo = {}
    
    if n in memo:
        return memo[n]
    
    if n == 0:
        result = 0
    elif n == 1:
        result = 0
    else:
        result = fibfib_naive(n-1, memo) + fibfib_naive(n-2, memo) + fibfib_naive(n-3, memo)
    
    memo[n] = result
    return result
def fibfib(n: int) -> int:
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
    return fibfib_naive(n)