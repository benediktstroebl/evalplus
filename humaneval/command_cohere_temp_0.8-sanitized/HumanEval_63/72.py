from typing import List
def fibfib_recursive(n: int, prev_vals: List[int] = None) -> int:
    """Compute the n-th FibFib number in a recursive manner."""
    if n == 0:
        return 0
    if n == 1:
        return 0
    if prev_vals is None:
        prev_vals = [0, 0]

    if n >= len(prev_vals):
        # Base case for recursion
        return fibfib_recursive(n - 1, prev_vals) + fibfib_recursive(n - 2, prev_vals) + fibfib_recursive(n - 3, prev_vals)
    else:
        # Recursive case
        return fibfib_recursive(n - 1, prev_vals) + fibfib_recursive(n - 2, prev_vals) + fibfib_recursive(n - 3, prev_vals)
def fibfib(n: int) -> int:
    """Compute the n-th FibFib number efficiently."""
    if n == 0:
        return 0
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibfib_recursive(n)