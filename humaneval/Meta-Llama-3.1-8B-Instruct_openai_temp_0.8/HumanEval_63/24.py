```markdown
**FibFib Number Sequence**
==========================

The FibFib number sequence is a sequence similar to the Fibonacci sequence that's defined as follows:
- `fibfib(0) == 0`
- `fibfib(1) == 0`
- `fibfib(2) == 1`
- `fibfib(n) == fibfib(n-1) + fibfib(n-2) + fibfib(n-3)`

**Efficient Computation**
------------------------

We can use memoization to efficiently compute the FibFib number sequence.

```python
def fibfib(n: int) -> int:
    """
    Compute the n-th element of the FibFib number sequence.

    Args:
    n (int): The index of the element to compute.

    Returns:
    int: The n-th element of the FibFib number sequence.
    """
    # Create a dictionary to store computed values
    memo = {0: 0, 1: 0, 2: 1}

    def fibfib_helper(k: int) -> int:
        # If the value is already computed, return it
        if k in memo:
            return memo[k]

        # Compute the value and store it in the memo dictionary
        result = fibfib_helper(k - 1) + fibfib_helper(k - 2) + fibfib_helper(k - 3)
        memo[k] = result
        return result

    return fibfib_helper(n)


# Test the function
print(fibfib(1))   # Output: 0
print(fibfib(5))   # Output: 4
print(fibfib(8))   # Output: 24
```

This script uses a helper function `fibfib_helper` to recursively compute the FibFib number sequence. The computed values are stored in a dictionary `memo` to avoid redundant computations. This approach has a time complexity of O(n), which is more efficient than the naive recursive approach with a time complexity of O(2^n).