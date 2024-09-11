```markdown
### FibFib Number Sequence
#### Efficiently Computing the n-th Element

The FibFib number sequence is a sequence similar to the Fibonacci sequence, defined as follows:
- `fibfib(0) == 0`
- `fibfib(1) == 0`
- `fibfib(2) == 1`
- `fibfib(n) == fibfib(n-1) + fibfib(n-2) + fibfib(n-3)`

```python
def fibfib(n: int) -> int:
    """
    Computes the n-th element of the FibFib number sequence.

    Args:
    n (int): The position of the element in the sequence.

    Returns:
    int: The n-th element of the FibFib number sequence.

    Raises:
    ValueError: If n is less than 0.
    """
    if n < 0:
        raise ValueError("n must be a non-negative integer")
    elif n == 0 or n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        # Create a list to store the sequence
        sequence = [0, 0, 1]
        
        # Compute the sequence up to the n-th element
        for i in range(3, n + 1):
            sequence.append(sequence[i - 1] + sequence[i - 2] + sequence[i - 3])
        
        return sequence[n]

# Test the function
print(fibfib(1))  # Output: 0
print(fibfib(5))  # Output: 4
print(fibfib(8))  # Output: 24
```

This script uses a dynamic approach to compute the n-th element of the FibFib number sequence. It initializes a list with the first three elements of the sequence (0, 0, 1), and then iteratively computes the remaining elements by adding the previous three elements. The function raises a ValueError if n is less than 0.