Here is a Python script that uses dynamic programming to efficiently compute the n-th element of the fib4 number sequence:
```python
def fib4(n: int):
    """
    The Fib4 number sequence is a sequence similar to the Fibonacci sequence that's defined as follows:
    fib4(0) -> 0
    fib4(1) -> 0
    fib4(2) -> 2
    fib4(3) -> 0
    fib4(n) -> fib4(n-1) + fib4(n-2) + fib4(n-3) + fib4(n-4).

    Args:
        n (int): The index of the element to compute in the fib4 sequence.

    Returns:
        int: The n-th element of the fib4 number sequence.

    Raises:
        ValueError: If n is a negative integer.
    """
    if n < 0:
        raise ValueError("n must be a non-negative integer")

    # Base cases
    if n == 0:
        return 0
    elif n == 1:
        return 0
    elif n == 2:
        return 2

    # Initialize a list to store the computed elements
    fib4_sequence = [0] * (n + 1)

    # Initialize the base cases
    fib4_sequence[0] = 0
    fib4_sequence[1] = 0
    fib4_sequence[2] = 2

    # Compute the elements iteratively
    for i in range(3, n + 1):
        fib4_sequence[i] = fib4_sequence[i - 1] + fib4_sequence[i - 2] + fib4_sequence[i - 3] + fib4_sequence[i - 4]

    return fib4_sequence[n]

# Test cases
print(fib4(5))  # Expected output: 4
print(fib4(6))  # Expected output: 8
print(fib4(7))  # Expected output: 14
```
This script uses a dynamic programming approach to compute the n-th element of the fib4 sequence. It initializes a list to store the computed elements and iteratively computes each element based on the previous four elements. The base cases are handled separately to avoid unnecessary computations. The function returns the n-th element of the fib4 sequence and raises a ValueError if n is a negative integer.