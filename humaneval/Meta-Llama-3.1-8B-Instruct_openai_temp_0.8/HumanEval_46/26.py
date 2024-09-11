```markdown
## Fib4 Number Sequence Computation
### A Python Script to Efficiently Compute the n-th Element of Fib4 Sequence

```python
def fib4(n: int):
    """
    The Fib4 number sequence is a sequence similar to the Fibbonacci sequence
    that's defined as follows:
    fib4(0) -> 0
    fib4(1) -> 0
    fib4(2) -> 2
    fib4(3) -> 0
    fib4(n) -> fib4(n-1) + fib4(n-2) + fib4(n-3) + fib4(n-4).

    This function efficiently computes the n-th element of the fib4 number sequence.
    It uses dynamic programming to store and reuse previously computed values.

    Args:
        n (int): The position of the element in the fib4 sequence.

    Returns:
        int: The n-th element of the fib4 sequence.
    """
    if n <= 3:  # Base cases
        return [0, 0, 2, 0][n]

    fib4_sequence = [0] * (n + 1)
    fib4_sequence[1] = 0
    fib4_sequence[2] = 2
    fib4_sequence[3] = 0

    for i in range(4, n + 1):  # Compute the sequence iteratively
        fib4_sequence[i] = fib4_sequence[i - 1] + fib4_sequence[i - 2] + fib4_sequence[i - 3] + fib4_sequence[i - 4]

    return fib4_sequence[n]

# Test the function
print(fib4(5))  # Output: 4
print(fib4(6))  # Output: 8
print(fib4(7))  # Output: 14
```

### Explanation

This script uses dynamic programming to efficiently compute the n-th element of the fib4 sequence. It stores previously computed values in a list `fib4_sequence` and reuses them to compute the next values, avoiding redundant computations and reducing the time complexity to O(n).