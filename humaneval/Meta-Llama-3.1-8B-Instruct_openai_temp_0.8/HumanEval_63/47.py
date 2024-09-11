### FibFib Number Sequence
#### Efficient Computation of the n-th Element

Below is a Python function that efficiently computes the n-th element of the FibFib number sequence using dynamic programming and memoization.

```python
def fibfib(n: int, memo: dict = {}) -> int:
    """Compute the n-th element of the FibFib number sequence.

    Args:
    n (int): The index of the element to compute.
    memo (dict): A dictionary to store intermediate results (default is an empty dictionary).

    Returns:
    int: The n-th element of the FibFib number sequence.
    """
    # Base cases
    if n == 0 or n == 1:
        return 0
    elif n == 2:
        return 1
    # Check if result is already memoized
    elif n in memo:
        return memo[n]
    # Compute and memoize result
    else:
        result = fibfib(n-1, memo) + fibfib(n-2, memo) + fibfib(n-3, memo)
        memo[n] = result
        return result

# Example usage
print(fibfib(1))   # Output: 0
print(fibfib(5))   # Output: 4
print(fibfib(8))   # Output: 24
```

This function uses a dictionary `memo` to store intermediate results, which avoids redundant computations and makes the function more efficient. The function's time complexity is O(n), and its space complexity is also O(n) due to the memoization.