```python
def fibfib(n: int) -> int:
    """
    The FibFib number sequence is a sequence similar to the Fibonacci sequence that's defined as follows:
    fibfib(0) == 0
    fibfib(1) == 0
    fibfib(2) == 1
    fibfib(n) == fibfib(n-1) + fibfib(n-2) + fibfib(n-3).

    Args:
        n (int): The position of the number in the sequence.

    Returns:
        int: The nth number in the FibFib sequence.

    Raises:
        ValueError: If n is less than 0.

    >>> fibfib(1)
    0
    >>> fibfib(5)
    4
    >>> fibfib(8)
    24
    """
    if n < 0:
        raise ValueError("Input must be a non-negative integer.")

    # Base cases
    if n == 0 or n == 1:
        return 0
    elif n == 2:
        return 1

    # Create a dictionary to store computed values for memoization
    memo = {0: 0, 1: 0, 2: 1}

    # Use memoization to compute the nth number in the sequence
    for i in range(3, n + 1):
        memo[i] = memo[i - 1] + memo[i - 2] + memo[i - 3]

    return memo[n]


if __name__ == "__main__":
    print(fibfib(1))  # Output: 0
    print(fibfib(5))  # Output: 4
    print(fibfib(8))  # Output: 24
```

This script uses memoization to efficiently compute the nth number in the FibFib sequence by storing previously computed values in a dictionary. This approach avoids redundant calculations and reduces the time complexity of the function.