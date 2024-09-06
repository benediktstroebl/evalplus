def fibfib(n: int):
    if n < 0:
        raise ValueError("FibFib sequence is not defined for negative numbers")
    elif n < 3:
        return n == 0 or n == 1  # Special cases
    else:
        return fibfib(n-1) + fibfib(n-2) + fibfib(n-3)