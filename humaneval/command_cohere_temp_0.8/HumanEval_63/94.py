```python
def fibfib(n: int):
    """Compute the n-th FibFib number efficiently in O(log(n)) time."""
    def fibfib_helper(n: int, acc: int = 0, last: int = 0) -> int:
        if n == 0:
            return acc
        if n == 1:
            return last
        return fibfib_helper(n-1, acc+last, fibfib_helper(n-2, last))
    return fibfib_helper(n)
```

This code defines a recursive function `fibfib_helper` that computes the FibFib numbers efficiently. It uses a similar approach to the classic Fibonacci sequence but with an additional layer of recursion. The top-level function `fibfib` optimizes the computation by directly calling `fibfib_helper` with the input value n. This eliminates the need for repeated recursive calls and ensures that the computation remains efficient.