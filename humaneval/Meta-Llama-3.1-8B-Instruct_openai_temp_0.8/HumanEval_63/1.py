### Efficiently Computing the n-th Element of the FibFib Number Sequence

We can efficiently compute the n-th element of the FibFib number sequence using memoization to store the previously computed values.

```python
def fibfib(n: int) -> int:
    """
    The FibFib number sequence is a sequence similar to the Fibonacci sequence that's defined as follows:
    fibfib(0) == 0
    fibfib(1) == 0
    fibfib(2) == 1
    fibfib(n) == fibfib(n-1) + fibfib(n-2) + fibfib(n-3).

    Args:
        n (int): The position of the element in the sequence.

    Returns:
        int: The n-th element of the FibFib number sequence.

    Examples:
        >>> fibfib(1)
        0
        >>> fibfib(5)
        4
        >>> fibfib(8)
        24
    """
    # Create a dictionary to store the computed values
    memo = {0: 0, 1: 0, 2: 1}

    def fibfib_helper(k: int) -> int:
        # If the value is already computed, return it
        if k in memo:
            return memo[k]
        # Otherwise, compute the value and store it in the memo
        else:
            result = fibfib_helper(k-1) + fibfib_helper(k-2) + fibfib_helper(k-3)
            memo[k] = result
            return result

    # Call the helper function to compute the n-th element
    return fibfib_helper(n)
```

This script uses a helper function `fibfib_helper` to compute the n-th element recursively, with memoization stored in the `memo` dictionary to avoid redundant computations. The main function `fibfib` initializes the memo and calls the helper function.

### Time Complexity:

The time complexity of this script is O(n), as it only needs to compute each element once and stores it in the memo for future reference.

### Space Complexity:

The space complexity of this script is also O(n), as the memo dictionary can store up to n elements.