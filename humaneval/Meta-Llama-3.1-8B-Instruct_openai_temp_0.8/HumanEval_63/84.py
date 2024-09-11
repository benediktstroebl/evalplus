### Efficiently Computing the FibFib Sequence
```python
def fibfib(n: int) -> int:
    """
    The FibFib number sequence is a sequence similar to the Fibonacci sequence.
    It is defined as follows:
    - fibfib(0) == 0
    - fibfib(1) == 0
    - fibfib(2) == 1
    - fibfib(n) == fibfib(n-1) + fibfib(n-2) + fibfib(n-3)

    Args:
        n (int): The index of the FibFib number to compute.

    Returns:
        int: The n-th element of the FibFib sequence.

    Example:
        >>> fibfib(1)
        0
        >>> fibfib(5)
        4
        >>> fibfib(8)
        24
    """

    # Handle base cases
    if n == 0 or n == 1:
        return 0
    elif n == 2:
        return 1

    # Initialize a dictionary to store computed values
    memo = {0: 0, 1: 0, 2: 1}

    # Compute and store the FibFib sequence up to the nth element
    for i in range(3, n + 1):
        # Use memoization to avoid redundant computation
        memo[i] = memo[i-1] + memo[i-2] + memo[i-3]

    # Return the computed nth element
    return memo[n]

# Test the function
print(fibfib(1))  # 0
print(fibfib(5))  # 4
print(fibfib(8))  # 24
```
This script uses a bottom-up dynamic programming approach with memoization to efficiently compute the nth element of the FibFib sequence. It handles base cases and stores computed values in a dictionary to avoid redundant computation. The script includes example use cases to demonstrate its correctness.