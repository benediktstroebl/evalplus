### Fib4 Number Sequence
#### Compute the n-th element of the fib4 number sequence efficiently.

```python
def fib4(n: int):
    """
    Compute the n-th element of the fib4 number sequence.

    The Fib4 number sequence is defined as follows:
    fib4(0) -> 0
    fib4(1) -> 0
    fib4(2) -> 2
    fib4(3) -> 0
    fib4(n) -> fib4(n-1) + fib4(n-2) + fib4(n-3) + fib4(n-4).

    Args:
        n (int): The index of the element in the fib4 sequence.

    Returns:
        int: The n-th element of the fib4 sequence.

    Raises:
        ValueError: If n is a negative integer.
    """
    if n < 0:
        raise ValueError("n must be a non-negative integer")

    # Base cases
    if n == 0 or n == 1:
        return 0
    elif n == 2:
        return 2
    elif n == 3:
        return 0

    # Initialize a list to store the fib4 sequence
    fib4_seq = [0, 0, 2, 0]

    # Compute the fib4 sequence up to the n-th element
    for i in range(4, n + 1):
        fib4_seq.append(fib4_seq[i - 1] + fib4_seq[i - 2] + fib4_seq[i - 3] + fib4_seq[i - 4])

    return fib4_seq[n]

# Test cases
print(fib4(5))   # Output: 4
print(fib4(6))   # Output: 8
print(fib4(7))   # Output: 14
```

This script defines a function `fib4` that takes an integer `n` as input and returns the n-th element of the fib4 number sequence. The function uses a list to store the sequence and computes each element iteratively using a loop. The base cases are handled separately to avoid unnecessary computations.