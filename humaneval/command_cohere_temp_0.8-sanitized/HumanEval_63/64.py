def fibfib(n: int):
    """Compute the n-th FibFib number efficiently in O(log n) time."""
    def fibfib_helper(n: int, acc: int = 0, prev: int = 0, curr: int = 1):
        if n == 0:
            return acc
        if n == 1:
            return prev
        if n == 2:
            return curr
        return fibfib_helper(n - 1, acc + prev, curr, acc + prev + curr)

    return fibfib_helper(n)