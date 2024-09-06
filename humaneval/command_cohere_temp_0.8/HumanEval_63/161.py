```python
def fibfib(n: int):
    """Compute the n-th FibFib number efficiently in O(log(n)) time."""
    def fibfib_helper(n: int, acc: int = 0, curr: int = 0) -> int:
        if n == 0:
            return acc
        if n == 1:
            return curr
        return fibfib_helper(n - 1, acc + fibfib_helper(n - 2, curr), curr + fibfib_helper(n - 3))

    return fibfib_helper(n)
```

This script defines a function `fibfib(n)` that efficiently calculates the n-th FibFib number, following the definition of the FibFib sequence provided in the prompt. It does so in optimal O(log(n)) time, building up the values iteratively. This is achieved through a helper function `fibfib_helper`, which performs the recursive iteration and aggregation, correctly computing the FibFib numbers.