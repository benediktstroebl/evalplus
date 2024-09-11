```markdown
## Efficiently Computing the FibFib Number Sequence in Python

This script uses memoization to efficiently compute the `n-th` element of the FibFib number sequence.

### Code
```python
def fibfib(n: int) -> int:
    """
    The FibFib number sequence is a sequence similar to the Fibonacci sequence 
    that's defined as follows:
    fibfib(0) == 0
    fibfib(1) == 0
    fibfib(2) == 1
    fibfib(n) == fibfib(n-1) + fibfib(n-2) + fibfib(n-3).

    Args:
        n (int): The position of the number in the sequence.

    Returns:
        int: The `n-th` number in the FibFib sequence.
    """
    # Create a dictionary to store the sequence values
    memo = {0: 0, 1: 0, 2: 1}

    def helper(k: int) -> int:
        # If the value is already in the memo, return it
        if k in memo:
            return memo[k]
        # Otherwise, compute the value and store it in the memo
        else:
            result = helper(k-1) + helper(k-2) + helper(k-3)
            memo[k] = result
            return result

    # Check if n is a non-negative integer
    if not isinstance(n, int) or n < 0:
        raise ValueError("Input must be a non-negative integer.")

    return helper(n)

# Example usage:
print(fibfib(1))   # Output: 0
print(fibfib(5))   # Output: 4
print(fibfib(8))   # Output: 24
```

### Explanation

The `fibfib` function uses a helper function (`helper`) to compute the `n-th` number in the sequence. The `helper` function uses memoization to avoid redundant computations.

We first create a dictionary `memo` to store the sequence values for `n = 0, 1, 2`. Then, we define the `helper` function, which checks if the value is already in the `memo` dictionary. If it is, we return the stored value. Otherwise, we compute the value by recursively calling the `helper` function for `k-1`, `k-2`, and `k-3`, and store the result in the `memo` dictionary.

Finally, we check if the input `n` is a non-negative integer and call the `helper` function to compute the `n-th` number in the sequence.