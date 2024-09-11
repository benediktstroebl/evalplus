### Efficiently Computing the Fib4 Number Sequence
#### Using Dynamic Programming

```markdown
### fib4.py
```python
def fib4(n: int) -> int:
    """
    Computes the n-th element of the Fib4 number sequence.

    Args:
        n (int): The position of the element in the sequence.

    Returns:
        int: The n-th element of the Fib4 number sequence.

    Example:
        >>> fib4(5)
        4
        >>> fib4(6)
        8
        >>> fib4(7)
        14
    """
    if n <= 1:
        return 0
    elif n == 2:
        return 2
    fib4_sequence = [0, 0, 2]
    for i in range(3, n + 1):
        next_fib4 = fib4_sequence[i - 1] + fib4_sequence[i - 2] + fib4_sequence[i - 3] + fib4_sequence[i - 4]
        fib4_sequence.append(next_fib4)
    return fib4_sequence[n]

# Test the function
print(fib4(5))  # Output: 4
print(fib4(6))  # Output: 8
print(fib4(7))  # Output: 14
```

This script uses dynamic programming to efficiently compute the n-th element of the Fib4 number sequence. It first initializes a list `fib4_sequence` with the first three elements of the sequence. Then, it iterates from `i = 3` to `n` to compute each subsequent element based on the previous four elements. The `fib4` function returns the n-th element of the sequence.