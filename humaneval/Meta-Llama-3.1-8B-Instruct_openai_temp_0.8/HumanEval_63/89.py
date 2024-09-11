### FibFib Number Sequence
#### A Python Function to Compute the n-th Element

Here's a Python function that uses dynamic programming to efficiently compute the n-th element of the FibFib number sequence.

```python
def fibfib(n: int) -> int:
    """
    Compute the n-th element of the FibFib number sequence.

    The FibFib number sequence is defined as:
    fibfib(0) == 0
    fibfib(1) == 0
    fibfib(2) == 1
    fibfib(n) == fibfib(n-1) + fibfib(n-2) + fibfib(n-3)

    Args:
        n (int): The index of the element to compute.

    Returns:
        int: The n-th element of the FibFib number sequence.
    """
    if n < 0:
        raise ValueError("n must be a non-negative integer")

    # Base cases
    if n == 0:
        return 0
    elif n == 1:
        return 0
    elif n == 2:
        return 1

    # Initialize a list to store the computed elements
    fibfib_sequence = [0, 0, 1]

    # Compute the elements from the 3rd to the n-th
    for i in range(3, n + 1):
        # Compute the i-th element as the sum of the previous three elements
        fibfib_sequence.append(fibfib_sequence[i - 1] + fibfib_sequence[i - 2] + fibfib_sequence[i - 3])

    # Return the n-th element
    return fibfib_sequence[n]

# Example usage:
print(fibfib(1))  # Output: 0
print(fibfib(5))  # Output: 4
print(fibfib(8))  # Output: 24
```

This function uses a list `fibfib_sequence` to store the computed elements of the FibFib number sequence. It initializes the list with the base cases and then iteratively computes the elements from the 3rd to the n-th. The time complexity of this function is O(n), making it efficient for large values of n.