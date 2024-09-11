### FibFib Number Sequence
#### A Python Script to Efficiently Compute the N-th Element

```python
def memoized_fibfib(n: int, memo: dict = {}):
    """
    Compute the n-th element of the FibFib number sequence efficiently using memoization.

    Args:
    n (int): The index of the element to compute.
    memo (dict): A dictionary to store previously computed values.

    Returns:
    int: The n-th element of the FibFib number sequence.
    """
    if n in memo:
        # If the value is already in the memo dictionary, return it
        return memo[n]
    elif n <= 0:
        # Base case: fibfib(0) == 0 and fibfib(1) == 0
        result = 0
    elif n == 2:
        # Base case: fibfib(2) == 1
        result = 1
    else:
        # Recursive case: fibfib(n) == fibfib(n-1) + fibfib(n-2) + fibfib(n-3)
        result = memoized_fibfib(n-1, memo) + memoized_fibfib(n-2, memo) + memoized_fibfib(n-3, memo)
    memo[n] = result  # Store the computed value in the memo dictionary
    return result


def fibfib(n: int):
    """
    Compute the n-th element of the FibFib number sequence.

    Args:
    n (int): The index of the element to compute.

    Returns:
    int: The n-th element of the FibFib number sequence.
    """
    return memoized_fibfib(n)


# Test the function
print(fibfib(1))  # Output: 0
print(fibfib(5))  # Output: 4
print(fibfib(8))  # Output: 24
```

This script uses a helper function `memoized_fibfib` to efficiently compute the n-th element of the FibFib number sequence using memoization. The `fibfib` function then calls `memoized_fibfib` with an empty dictionary as the `memo` argument. The `memoized_fibfib` function stores previously computed values in the `memo` dictionary to avoid redundant computations.

Note that this script uses a bottom-up approach, where it recursively computes the values from `n-3` to `n`. This approach has a time complexity of O(n), which is more efficient than a naive recursive approach that has a time complexity of O(2^n).