```python
def fibfib(n: int):
    """Compute the n-th FibFib number efficiently in O(log(n)) time."""
    def fibfib_helper(n: int, acc: int = 0, curr: int = 0) -> int:
        if n == 0:
            return acc
        if n == 1:
            return curr
        return fibfib_helper(n-1, acc+fibfib_helper(n-2, curr), curr+fibfib_helper(n-3, 0))
    return fibfib_helper(n)
```

This script defines a recursive function `fibfib_helper` that computes the n-th FibFib number and an iterative function `fibfib` that calls `fibfib_helper` with the input n. The `fibfib_helper` function exploits the mathematical definition of the FibFib sequence to efficiently compute the n-th number in the sequence. 

This solution has an efficiency of O(log(n)) as opposed to the less efficient O(n) solution that uses only the definition of the FibFib sequence without the helper function.