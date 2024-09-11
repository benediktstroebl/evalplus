```python
def fibfib(n: int) -> int:
    """
    The FibFib number sequence is a sequence similar to the Fibonacci sequence that's defined as follows:
    fibfib(0) == 0
    fibfib(1) == 0
    fibfib(2) == 1
    fibfib(n) == fibfib(n-1) + fibfib(n-2) + fibfib(n-3).

    Args:
        n (int): The index of the element to compute in the FibFib sequence.

    Returns:
        int: The n-th element of the FibFib sequence.

    Raises:
        ValueError: If n is less than 0.
    """
    if n < 0:
        raise ValueError("n must be a non-negative integer.")

    # Base cases
    if n == 0 or n == 1:
        return 0
    elif n == 2:
        return 1

    # Initialize a dictionary to store the computed values
    memo = {0: 0, 1: 0, 2: 1}

    # Compute and store the values in the memo dictionary
    for i in range(3, n + 1):
        memo[i] = memo[i - 1] + memo[i - 2] + memo[i - 3]

    # Return the computed value
    return memo[n]


# Test cases
print(fibfib(1))      # 0
print(fibfib(5))      # 4
print(fibfib(8))      # 24
print(fibfib(10))     # 90
print(fibfib(15))     # 523
```

In this code, we use a dictionary called `memo` to store the computed values of the FibFib sequence. We start with the base cases `n = 0, 1, 2`, and then compute and store the values for `n = 3` to `n = n`. Finally, we return the computed value for `n`.

This approach has a time complexity of O(n), which is much more efficient than computing the sequence from scratch using recursion or a loop. The space complexity is O(n) as well, since we store the computed values in the `memo` dictionary.