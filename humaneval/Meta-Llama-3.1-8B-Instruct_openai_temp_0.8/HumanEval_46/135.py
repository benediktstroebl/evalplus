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
        n (int): The position of the number in the sequence.

    Returns:
        int: The nth element of the Fib4 number sequence.
    """
    if n < 4:
        # Base cases
        return [0, 0, 2][n]

    # Initialize the list to store the sequence
    fib4_sequence = [0] * (n + 1)
    fib4_sequence[1] = 0
    fib4_sequence[2] = 2
    fib4_sequence[3] = 0

    # Compute the sequence iteratively
    for i in range(4, n + 1):
        fib4_sequence[i] = fib4_sequence[i-1] + fib4_sequence[i-2] + fib4_sequence[i-3] + fib4_sequence[i-4]

    return fib4_sequence[n]


# Test cases
print(fib4(5))  # Output: 4
print(fib4(6))  # Output: 8
print(fib4(7))  # Output: 14
```