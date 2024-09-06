def fibfib(n):
    prev1, prev2, prev3 = 0, 1, 0
    if n >= 1:
        prev1 = 0
    if n >= 2:
        prev2 = 1
    if n >= 3:
        prev3 = 0
    for i in range(4, n + 1):
        prev3, prev2, prev1 = prev2, prev1 + prev2, prev3 + prev1
    return prev1