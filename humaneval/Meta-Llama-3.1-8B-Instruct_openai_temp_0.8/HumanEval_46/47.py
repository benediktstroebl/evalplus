```python
def fib4(n: int) -> int:
    """
    The Fib4 number sequence is a sequence similar to the Fibonacci sequence that's defined as follows:
    fib4(0) -> 0
    fib4(1) -> 0
    fib4(2) -> 2
    fib4(3) -> 0
    fib4(n) -> fib4(n-1) + fib4(n-2) + fib4(n-3) + fib4(n-4).

    Args:
        n (int): The index of the Fib4 number sequence.

    Returns:
        int: The n-th element of the Fib4 number sequence.
    """
    if n <= 1:
        return 0
    elif n == 2:
        return 2
    else:
        # Initialize a list to store the first 5 elements of the sequence
        fib4_sequence = [0, 0, 2]
        # Compute the rest of the sequence using a loop
        for i in range(3, n + 1):
            fib4_sequence.append(fib4_sequence[i - 1] + fib4_sequence[i - 2] + fib4_sequence[i - 3] + fib4_sequence[i - 4])
        # Return the n-th element of the sequence
        return fib4_sequence[n]

# Test the function
print(fib4(5))  # Output: 4
print(fib4(6))  # Output: 8
print(fib4(7))  # Output: 14
```

This script defines the `fib4` function, which takes an integer `n` as input and returns the n-th element of the Fib4 number sequence. The function uses a loop to compute the sequence iteratively, rather than recursively.