from collections import Sequence
def fibfib_iter(n: int, memo: Sequence = None):
    if n < 0:
        raise ValueError("FibFib is only defined for non-negative integers")
    if n == 0:
        return 0
    if n == 1:
        return 0
    if memo is None:
        memo = []
    if n in memo:
        return memo[n]
    memo[n] = fibfib_iter(n - 1, memo) + fibfib_iter(n - 2, memo) + fibfib_iter(n - 3, memo)
    return memo[n]
def fibfib(n: int):
    return fibfib_iter(n)