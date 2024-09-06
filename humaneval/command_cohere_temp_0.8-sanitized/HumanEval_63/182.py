def fibfib(n: int):
    prev1, prev2, fibfib_number = 0, 0, 0
    while n >= 3:
        fibfib_number = prev1 + prev2 + fibfib_number
        prev2, prev1 = prev1, fibfib_number
        n -= 1
    if n == 2:
        fibfib_number += prev2
    elif n == 1:
        fibfib_number += prev1
    return fibfib_number