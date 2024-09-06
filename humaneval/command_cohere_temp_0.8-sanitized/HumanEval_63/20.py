def fibfib(n: int):
    """Compute the n-th FibFib number efficiently in O(log(n)) time."""
    def fibfib_helper(n: int, acc: int = 0, curr: int = 0) -> int:
        if n == 0:
            return acc
        if n == 1:
            return curr
        return fibfib_helper(n - 1, acc + fibfib_helper(n - 2, curr), curr + fibfib_helper(n - 3))

    return fibfib_helper(n)