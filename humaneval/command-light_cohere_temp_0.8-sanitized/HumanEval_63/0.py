def fibfib(n: int) -> int:
    if n == 0:  # base case
        return 0
    elif n == 1:  # base case
        return 0
    else:
        return fibfib(n-1) + fibfib(n-2) + fibfib(n-3)