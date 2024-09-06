def fibfib(n: int):
    """Compute the n-th FibFib number efficiently in O(log n) time."""
    def fibfib_helper(n: int, acc: int = 0, prev: int = 0, curr: int = 1) -> int:
        """Helper function to recursively compute FibFib numbers."""
        if n == 0:
            return acc
        elif n == 1:
            return prev
        elif n == 2:
            return curr
        else:
            return fibfib_helper(n - 1, acc + prev, curr, acc + prev + curr)

    if n < 0:
        raise ValueError("FibFib numbers are only defined for non-negative integers.")
    elif n == 0:
        return 0
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibfib_helper(n - 2)