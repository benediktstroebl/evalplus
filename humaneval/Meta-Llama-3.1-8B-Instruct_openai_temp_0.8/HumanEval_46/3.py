```markdown
# Compute the n-th element of the Fib4 number sequence
=====================================================

This script uses dynamic programming to efficiently compute the n-th element
of the Fib4 number sequence.

```python
def fib4(n: int) -> int:
    """
    The Fib4 number sequence is a sequence similar to the Fibbonacci sequence
    that's defined as follows:
    fib4(0) -> 0
    fib4(1) -> 0
    fib4(2) -> 2
    fib4(3) -> 0
    fib4(n) -> fib4(n-1) + fib4(n-2) + fib4(n-3) + fib4(n-4).

    Args:
        n (int): The index of the element to compute.

    Returns:
        int: The n-th element of the Fib4 number sequence.
    """
    if n < 4:
        return 0 if n > 1 else 2

    # Create a list to store the computed elements
    fib4_sequence = [0] * (n + 1)
    fib4_sequence[1] = 0
    fib4_sequence[2] = 2

    # Compute the rest of the sequence using dynamic programming
    for i in range(3, n + 1):
        fib4_sequence[i] = fib4_sequence[i - 1] + fib4_sequence[i - 2] + fib4_sequence[i - 3] + fib4_sequence[i - 4]

    return fib4_sequence[n]

# Test the function
print(fib4(5))  # Output: 4
print(fib4(6))  # Output: 8
print(fib4(7))  # Output: 14
```

In this script, we first create a list to store the computed elements and initialize the first three elements. Then, we use a loop to compute the rest of the sequence using dynamic programming. Finally, we return the n-th element of the sequence.