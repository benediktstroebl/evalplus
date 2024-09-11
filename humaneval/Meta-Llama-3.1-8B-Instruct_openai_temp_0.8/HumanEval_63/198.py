```markdown
### FibFib Number Sequence
#### Efficiently Computing the n-th Element

The FibFib number sequence is a sequence similar to the Fibonacci sequence, but with a different recurrence relation.

#### Solution

```python
def fibfib(n: int) -> int:
    """
    Compute the n-th element of the FibFib number sequence.

    Args:
        n (int): The index of the element to compute.

    Returns:
        int: The n-th element of the FibFib number sequence.

    Raises:
        ValueError: If n is a negative integer.
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

    # Initialize the first three elements of the sequence
    a, b, c = 0, 0, 1

    # Compute the sequence up to the n-th element
    for _ in range(2, n):
        # Update the last three elements of the sequence
        a, b, c = b, c, b + c + a

    return c
```

#### Example Use Cases

```python
print(fibfib(1))  # Output: 0
print(fibfib(5))  # Output: 4
print(fibfib(8))  # Output: 24
```

This solution uses a bottom-up dynamic programming approach to efficiently compute the n-th element of the FibFib number sequence. It starts by initializing the first three elements of the sequence and then iteratively updates the last three elements to compute the next element in the sequence. This approach has a time complexity of O(n) and a space complexity of O(1), making it much more efficient than a recursive approach for large values of n.