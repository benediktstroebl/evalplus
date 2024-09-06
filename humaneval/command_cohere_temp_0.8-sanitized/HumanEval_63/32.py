from itertools import accumulate
def fibfib_iter(n):
    if n == 0:
        return 0
    elif n == 1:
        return 0
    else:
        a, b, c = 0, 1, 0
        for i in range(2, n+1):
            a, b, c = b, a + b + c, c
        return a
def fibfib(n):
    return next(accumulate([0, 0, 1], fibfib_iter))[n]