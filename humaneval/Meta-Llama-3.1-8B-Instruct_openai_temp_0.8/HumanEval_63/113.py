Here's a Python script that uses memoization to efficiently compute the n-th element of the FibFib number sequence:
```python
def fibfib(n: int) -> int:
    """
    Compute the nth element of the FibFib number sequence.

    The FibFib number sequence is defined as follows:
    fibfib(0) == 0
    fibfib(1) == 0
    fibfib(2) == 1
    fibfib(n) == fibfib(n-1) + fibfib(n-2) + fibfib(n-3).

    Args:
        n (int): The index of the element to compute.

    Returns:
        int: The nth element of the FibFib number sequence.

    Example:
        >>> fibfib(1)
        0
        >>> fibfib(5)
        4
        >>> fibfib(8)
        24
    """
    if n < 0:
        raise ValueError("n must be a non-negative integer")
    if n == 0 or n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        memo = {0: 0, 1: 0, 2: 1}  # Initialize memoization dictionary
        for i in range(3, n + 1):
            memo[i] = memo[i - 1] + memo[i - 2] + memo[i - 3]
        return memo[n]

# Test the function
print(fibfib(1))  # Output: 0
print(fibfib(5))  # Output: 4
print(fibfib(8))  # Output: 24
```
This script uses a dictionary called `memo` to store the previously computed values of the FibFib sequence. This way, when we need to compute the `n`-th element, we can simply look up the value in the `memo` dictionary instead of recomputing it from scratch. This makes the function much more efficient for large values of `n`.

Note that the `memo` dictionary is initialized with the base cases of the FibFib sequence, and then we iterate over the range from `3` to `n`, computing each element and storing it in the `memo` dictionary. Finally, we return the value of the `n`-th element from the `memo` dictionary.