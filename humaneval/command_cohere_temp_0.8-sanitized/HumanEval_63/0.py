def fibfib(n):
    prev3, prev2, prev1, curr = 0, 0, 0, 0
    for _ in range(n):
        curr = prev3 + prev2 + prev1
        prev3 = prev2
        prev2 = prev1
        prev1 = curr
    return curr