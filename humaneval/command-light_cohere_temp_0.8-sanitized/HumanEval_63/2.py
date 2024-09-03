def fibfib(n: int) -> int:
    if n == 0:  # Base case: return 0
        return 0
    elif n == 1:  # Base case: return 0
        return 0
    else:
        return fibfib(n - 1) + fibfib(n - 2) + fibfib(n - 3)