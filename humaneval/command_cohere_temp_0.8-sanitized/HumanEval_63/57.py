from collections import Sequence
def fibfib_iter(n: int, memo = None):
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
    memo_add = fibfib_iter(n - 1, memo) + fibfib_iter(n - 2, memo)
    memo.append(memo_add)
    return memo_add
def fibfib(n: int):
    if not isinstance(n, int) or n < 0:
        raise ValueError("FibFib is only defined for non-negative integers")
    return fibfib_iter(n)