from itertools import accumulate
def fibfib_iter(n: int):
    if n == 0:
        return 0
    elif n == 1:
        return 0
    else:
        a, b = 0, 1
        for i in range(2, n + 1):
            a, b = b, a + b
        return b
def fibfib(n: int):
    if n < 0:
        raise ValueError("FibFib is defined only for non-negative integers")
    elif n == 0 or n == 1:
        return 0
    else:
        return next(accumulate(fibfib_iter(n), initial=0))