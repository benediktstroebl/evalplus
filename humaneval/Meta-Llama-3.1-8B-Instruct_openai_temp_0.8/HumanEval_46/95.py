```python
def fib4(n: int) -> int:
    """
    The Fib4 number sequence is a sequence similar to the Fibonacci sequence that's defined as follows:
    fib4(0) -> 0
    fib4(1) -> 0
    fib4(2) -> 2
    fib4(3) -> 0
    fib4(n) -> fib4(n-1) + fib4(n-2) + fib4(n-3) + fib4(n-4).

    This function efficiently computes the n-th element of the fib4 number sequence using dynamic programming.

    Args:
        n (int): The index of the element in the fib4 sequence.

    Returns:
        int: The nth element of the fib4 sequence.
    """

    # Handle edge cases where n is less than 0
    if n < 0:
        raise ValueError("n must be a non-negative integer")

    # Initialize a list to store the fib4 numbers
    fib4_numbers = [0, 0, 2, 0] + [0]*(n-3)

    # Compute the fib4 numbers up to the nth number
    for i in range(4, n+1):
        fib4_numbers[i-1] = fib4_numbers[i-2] + fib4_numbers[i-3] + fib4_numbers[i-4]

    # Return the nth fib4 number
    return fib4_numbers[n-1]


# Test cases
print(fib4(5))  # Output: 4
print(fib4(6))  # Output: 8
print(fib4(7))  # Output: 14
```

This script uses dynamic programming to efficiently compute the nth element of the fib4 number sequence. The `fib4_numbers` list stores the fib4 numbers up to the nth number, and the script updates this list iteratively to compute the next number in the sequence. The function then returns the nth fib4 number.