### Fib4 Number Sequence
#### Efficient Computation using Dynamic Programming

```python
def fib4(n: int) -> int:
    """
    Compute the n-th element of the Fib4 number sequence.

    The Fib4 number sequence is a sequence similar to the Fibbonacci sequence that's defined as follows:
    fib4(0) -> 0
    fib4(1) -> 0
    fib4(2) -> 2
    fib4(3) -> 0
    fib4(n) -> fib4(n-1) + fib4(n-2) + fib4(n-3) + fib4(n-4).

    Args:
        n (int): The index of the element to compute.

    Returns:
        int: The n-th element of the Fib4 number sequence.

    Raises:
        ValueError: If n is a negative integer.
    """
    if n < 0:
        raise ValueError("n must be a non-negative integer")
    elif n <= 3:
        return [0, 0, 2, 0][n]

    # Initialize a list to store the computed elements
    fib4_seq = [0] * (n + 1)
    fib4_seq[1] = 0
    fib4_seq[2] = 2
    fib4_seq[3] = 0

    # Compute the n-th element using dynamic programming
    for i in range(4, n + 1):
        fib4_seq[i] = fib4_seq[i - 1] + fib4_seq[i - 2] + fib4_seq[i - 3] + fib4_seq[i - 4]

    return fib4_seq[n]

# Test cases
print(fib4(5))  # Output: 4
print(fib4(6))  # Output: 8
print(fib4(7))  # Output: 14
```

This script defines a function `fib4(n)` that computes the n-th element of the Fib4 number sequence using dynamic programming. The function first checks if `n` is a non-negative integer and raises a `ValueError` if it's not. If `n` is less than or equal to 3, it returns the precomputed value. Otherwise, it initializes a list `fib4_seq` to store the computed elements and uses a loop to compute the n-th element. The function returns the n-th element of the Fib4 number sequence.