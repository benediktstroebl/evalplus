```python
def fib4(n: int):
    """
    The Fib4 number sequence is a sequence similar to the Fibbonacci sequence that's defined as follows:
    fib4(0) -> 0
    fib4(1) -> 0
    fib4(2) -> 2
    fib4(3) -> 0
    fib4(n) -> fib4(n-1) + fib4(n-2) + fib4(n-3) + fib4(n-4).

    Args:
        n (int): The position of the element in the sequence.

    Returns:
        int: The nth element of the fib4 sequence.
    """
    # Handle base cases
    if n <= 1:
        return 0
    elif n == 2:
        return 2
    elif n == 3:
        return 0

    # Initialize a list to store the sequence
    sequence = [0] * (n + 1)
    sequence[1] = 0
    sequence[2] = 2
    sequence[3] = 0

    # Compute the sequence iteratively
    for i in range(4, n + 1):
        sequence[i] = sequence[i-1] + sequence[i-2] + sequence[i-3] + sequence[i-4]

    # Return the nth element
    return sequence[n]

# Test cases
print(fib4(5))  # Output: 4
print(fib4(6))  # Output: 8
print(fib4(7))  # Output: 14
```

This script uses dynamic programming to efficiently compute the n-th element of the fib4 sequence. It initializes a list `sequence` with a size of `n+1`, where the first four elements are the base cases. It then iteratively computes each element of the sequence from the fifth element to the nth element, using the previously computed elements. Finally, it returns the nth element of the sequence.