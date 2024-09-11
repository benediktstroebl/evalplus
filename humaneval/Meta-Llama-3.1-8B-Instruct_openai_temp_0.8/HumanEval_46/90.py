### Self-Contained Python Script to Compute the Fib4 Number Sequence
```python
def fib4(n: int) -> int:
    """
    Compute the n-th element of the Fib4 number sequence.

    The Fib4 number sequence is a sequence similar to the Fibbonacci sequence
    that's defined as follows:
    fib4(0) -> 0
    fib4(1) -> 0
    fib4(2) -> 2
    fib4(3) -> 0
    fib4(n) -> fib4(n-1) + fib4(n-2) + fib4(n-3) + fib4(n-4).

    Args:
        n (int): The position of the element in the sequence.

    Returns:
        int: The n-th element of the Fib4 number sequence.
    """
    if n < 4:
        # Base cases
        if n == 0 or n == 1:
            return 0
        elif n == 2:
            return 2

    # Initialize a list to store the sequence
    fib4_sequence = [0, 0, 2] + [0] * (n - 2)

    # Compute the sequence iteratively
    for i in range(4, n + 1):
        fib4_sequence[i - 1] = fib4_sequence[i - 2] + fib4_sequence[i - 3] + fib4_sequence[i - 4]

    return fib4_sequence[n - 1]


# Example usage:
print(fib4(5))  # Output: 4
print(fib4(6))  # Output: 8
print(fib4(7))  # Output: 14
```
This script defines the `fib4` function, which uses an iterative approach to compute the n-th element of the Fib4 number sequence. It initializes a list to store the sequence and then iteratively computes the sequence up to the n-th element. The base cases for n <= 2 are handled directly, and the function returns the n-th element of the sequence.