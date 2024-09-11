### Efficiently Computing the Fib4 Sequence
#### Using Dynamic Programming

```markdown
### Code
```python
def fib4(n: int) -> int:
    """
    Compute the n-th element of the fib4 number sequence.

    Args:
    n (int): The index of the element in the fib4 sequence.

    Returns:
    int: The n-th element of the fib4 sequence.

    Raises:
    ValueError: If n is a negative integer.
    """
    if n < 0:
        raise ValueError("n must be a non-negative integer.")
    elif n <= 1:
        return 0
    elif n == 2:
        return 2
    elif n == 3:
        return 0
    else:
        # Initialize a list to store the fib4 sequence
        fib4_sequence = [0] * (n + 1)

        # Base cases
        fib4_sequence[0] = 0
        fib4_sequence[1] = 0
        fib4_sequence[2] = 2
        fib4_sequence[3] = 0

        # Compute the fib4 sequence iteratively
        for i in range(4, n + 1):
            fib4_sequence[i] = fib4_sequence[i - 1] + fib4_sequence[i - 2] + fib4_sequence[i - 3] + fib4_sequence[i - 4]

        # Return the n-th element of the fib4 sequence
        return fib4_sequence[n]

### Example Usage
print(fib4(5))  # Output: 4
print(fib4(6))  # Output: 8
print(fib4(7))  # Output: 14
```

#### Explanation

This script uses dynamic programming to efficiently compute the n-th element of the fib4 sequence. The `fib4` function initializes a list to store the sequence, starting with the base cases. Then it iteratively computes each element of the sequence using the recurrence relation `fib4(n) = fib4(n-1) + fib4(n-2) + fib4(n-3) + fib4(n-4)`. The function returns the n-th element of the sequence, which is stored in the `fib4_sequence` list.

This approach has a time complexity of O(n) and a space complexity of O(n), making it more efficient than a recursive solution for large values of n.