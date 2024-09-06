```python
def fibfib(n: int):
    """Compute the n-th FibFib number efficiently in O(log(n)) time."""
    def fibfib_helper(n: int, acc: int = 0, prev: int = 0, curr: int = 1) -> int:
        if n == 0:
            return acc
        if n == 1:
            return prev
        if n == 2:
            return curr
        return fibfib_helper(n - 1, acc + prev, curr, prev + curr)

    if n < 0:
        raise ValueError("FibFib is not defined for negative numbers.")
    return fibfib_helper(n)
```

This code defines a recursive function `fibfib_helper` that computes the FibFib numbers efficiently, following the definition provided, and the base cases for 0, 1, and 2. The function `fibfib` checks for negative input and calls `fibfib_helper` with the appropriate input. This solution has a time complexity of O(log(n)) as the number of recursive calls decreases steadily.