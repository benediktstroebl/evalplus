def fibfib(n: int):
    prev1, prev2, fibfib_num = 0, 0, 0
    while n > 0:
        fibfib_num = prev1 + prev2 + fibfib_num
        prev2, prev1 = prev1, fibfib_num
        n -= 1
    return fibfib_num