def fibfib(n: int):
    """Compute the n-th FibFib number efficiently in O(log(n)) time."""
    def fibfib_helper(n: int, acc: int = 0, val: int = 1):
        """Helper function that uses the doubling method to efficiently compute FibFib numbers."""
        if n == 0:
            return acc
        elif n == 1:
            return val
        else:
            return fibfib_helper(n // 2, acc + val, val + fibfib_helper(n // 2))

    # If n is 0 or 1, return the corresponding FibFib number
    if n < 2:
        return n
    # Otherwise, use the doubling method to compute the n-th FibFib number efficiently
    else:
        return fibfib_helper(n)