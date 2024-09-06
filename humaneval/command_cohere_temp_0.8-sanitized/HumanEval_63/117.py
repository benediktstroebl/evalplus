from itertools import accumulate
def fibfib_iter(n: int):
    if n == 0:
        return 0
    elif n == 1:
        return 0
    else:
        return next(acc for acc in accumulate([0, 0, 1]) if acc <= n)
def fibfib(n: int):
    if n < 0:
        raise ValueError("FibFib is only defined for non-negative integers.")
    return fibfib_iter(n)