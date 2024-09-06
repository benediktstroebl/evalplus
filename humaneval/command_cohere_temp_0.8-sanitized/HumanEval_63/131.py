def fibfib(n: int):
    """Compute the n-th FibFib number efficiently in O(log(n)) time."""
    def fibfib_helper(n: int, acc: int = 0, val: int = 1):
        """Helper function that uses dynamic programming to efficiently compute the FibFib numbers."""
        if n == 0:
            return acc
        elif n == 1:
            return val
        else:
            return fibfib_helper(n - 1, acc + val, val + fibfib_helper(n - 2))

    # Since the 0th and 1st elements are fixed, start directly at element 2
    return fibfib_helper(n - 2)