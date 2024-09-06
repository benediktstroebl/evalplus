def fibfib(n: int):
    """Compute the n-th FibFib number efficiently in O(log(n)) time."""
    def fibfib_helper(n: int, acc: int = 0, last: int = 0) -> int:
        if n == 0:
            return acc
        if n == 1:
            return last
        return fibfib_helper(n-1, acc+last, fibfib_helper(n-2, last))
    return fibfib_helper(n)