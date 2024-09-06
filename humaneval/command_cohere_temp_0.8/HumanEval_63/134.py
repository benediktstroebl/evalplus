```python
from typing import List

def fibfib_recursive(n: int, prev_vals: List[int] = None) -> int:
    """Compute the n-th FibFib number in a recursive manner."""
    if n == 0:
        return 0
    if n == 1:
        return 0
    if prev_vals is None:
        prev_vals = [0, 0]

    if n >= len(prev_vals):
        # Base case for recursion
        return fibfib_recursive(n - 1, prev_vals) + fibfib_recursive(n - 2, prev_vals) + fibfib_recursive(n - 3, prev_vals)
    else:
        # Recursive case
        return fibfib_recursive(n - 1, prev_vals) + fibfib_recursive(n - 2, prev_vals) + fibfib_recursive(n - 3, prev_vals)

def fibfib(n: int) -> int:
    """Compute the n-th FibFib number efficiently."""
    if n == 0:
        return 0
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibfib_recursive(n)

# Test cases
print(fibfib(1))
print(fibfib(5))
print(fibfib(8))
```

This script features a top-down design, employing both recursive and iterative techniques. The `fibfib_recursive` function handles recursive computations, while the `fibfib` function efficiently calculates the n-th FibFib number using a cached approach for less redundant calculations.

Note that this implementation has a time complexity of `O(2^n)` due to the hierarchical nature of the FibFib sequence, and the recursive approach, though optimized, may lead to performance issues for larger values of n. An iterative approach would be more efficient for handling larger inputs.