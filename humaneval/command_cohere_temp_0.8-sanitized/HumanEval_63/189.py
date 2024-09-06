from itertools import accumulate
def fibfib_iter(n: int):
    fibfib_0 = 0
    fibfib_1 = 0
    fibfib_2 = 1
    for i in range(3, n + 1):
        fibfib_i = fibfib_iter_helper(fibfib_0, fibfib_1, fibfib_2)
        fibfib_0, fibfib_1, fibfib_2 = fibfib_1, fibfib_2, fibfib_i
    return fibfib_2
def fibfib_iter_helper(f0, f1, f2):
    return f0 + f1 + f2
def fibfib(n: int):
    return next(accumulate(fibfib_iter(n), initial=0))