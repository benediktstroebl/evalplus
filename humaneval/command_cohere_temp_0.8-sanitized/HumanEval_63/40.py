from itertools import accumulate
def fibfib_iter(n: int):
    fibfib_0 = 0
    fibfib_1 = 0
    fibfib_2 = 1
    for i in range(3, n + 1):
        fibfib_i = fibfib_prev(fibfib_prev(fibfib_prev(fibfib_2, fibfib_1, fibfib_0)) + fibfib_1 + fibfib_0)
        fibfib_0, fibfib_1, fibfib_2 = fibfib_1, fibfib_2, fibfib_i
    return fibfib_2
def fibfib_prev(a, b, c):
    if a == 0:
        return b
    if b == 0:
        return c
    if c == 0:
        return a
    return fibfib_prev(a - b, b - c, c)
def fibfib(n: int):
    return next(accumulate(fibfib_iter(n), 0))