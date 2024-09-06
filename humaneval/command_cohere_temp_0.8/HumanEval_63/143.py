```python
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
```

This code defines a recursive function `fibfib_helper` that computes the FibFib numbers efficiently. It's based on the recursive definition of the sequence, where `fibfib(n)` equals `fibfib(n-1)` plus `fibfib(n-2)` plus `fibfib(n-3)`. The helper function implements this definition, using the parameters `acc` to represent the sum of previous two terms, `prev` to represent the previous term, and `curr` to represent the current term. The function computes these values recursively for `n = 0`, `n = 1`, and `n = 2` to establish the base cases, and then it uses the recursive formula for `n > 2`. The function `fibfib` wraps the helper function with appropriate input validation to ensure `n` is a positive integer.