```markdown
### FibFib Number Sequence
#### Efficient Computation of nth Element

The FibFib number sequence is a sequence similar to the Fibonacci sequence that's defined as follows:

- `fibfib(0) == 0`
- `fibfib(1) == 0`
- `fibfib(2) == 1`
- `fibfib(n) == fibfib(n-1) + fibfib(n-2) + fibfib(n-3)`

This script provides an efficient function to compute the nth element of the FibFib number sequence.

```python
def fibfib(n: int) -> int:
    """
    Compute the nth element of the FibFib number sequence.

    Args:
    n (int): The index of the element to compute.

    Returns:
    int: The nth element of the FibFib number sequence.

    Raises:
    ValueError: If n is a negative integer.
    """

    if n < 0:
        raise ValueError("n must be a non-negative integer.")

    if n <= 1:
        return 0
    elif n == 2:
        return 1

    # Initialize a list to store the computed elements
    fibfib_sequence = [0, 0, 1]

    # Compute the elements of the sequence up to the nth element
    for i in range(3, n + 1):
        # Compute the next element as the sum of the previous three elements
        next_element = fibfib_sequence[i - 1] + fibfib_sequence[i - 2] + fibfib_sequence[i - 3]
        # Append the next element to the sequence
        fibfib_sequence.append(next_element)

    # Return the nth element of the sequence
    return fibfib_sequence[n]


# Test cases
print(fibfib(1))  # Output: 0
print(fibfib(5))  # Output: 4
print(fibfib(8))  # Output: 24
```

### Time Complexity
The time complexity of this script is O(n), where n is the index of the element to compute. This is because we need to compute the elements of the sequence up to the nth element.

### Space Complexity
The space complexity of this script is also O(n), as we need to store the computed elements in a list.