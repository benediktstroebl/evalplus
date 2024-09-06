def fibfib(n: int):
    prev1, prev2, prev3 = 0, 0, 0
    if n >= 1:
        prev1 = fibfib(n-1)
    if n >= 2:
        prev2 = fibfib(n-2)
    if n >= 3:
        prev3 = fibfib(n-3)
    return prev1 + prev2 + prev3