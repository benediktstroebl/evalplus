from itertools import accumulate
def fibfib(n: int):
    return next(accumulate(fibfib_iter(n)))