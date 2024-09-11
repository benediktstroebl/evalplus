```python
def fib4(n: int) -> int:
    """
    The Fib4 number sequence is a sequence similar to the Fibbonacci sequnece that's defined as follows:
    fib4(0) -> 0
    fib4(1) -> 0
    fib4(2) -> 2
    fib4(3) -> 0
    fib4(n) -> fib4(n-1) + fib4(n-2) + fib4(n-3) + fib4(n-4).

    Args:
        n (int): The position of the element in the Fib4 number sequence.

    Returns:
        int: The n-th element of the Fib4 number sequence.
    """
    if n < 0:
        raise ValueError("n must be a non-negative integer")

    if n <= 2:
        return 0

    if n == 3:
        return 2

    # Initialize a list to store the first 4 elements of the sequence
    fib4_sequence = [0, 0, 2, 0]

    # Compute the rest of the sequence using dynamic programming
    for i in range(4, n + 1):
        # The next element is the sum of the previous 4 elements
        next_element = fib4_sequence[i - 1] + fib4_sequence[i - 2] + fib4_sequence[i - 3] + fib4_sequence[i - 4]
        fib4_sequence.append(next_element)

    return fib4_sequence[n]


# Test the function
print(fib4(5))  # Output: 4
print(fib4(6))  # Output: 8
print(fib4(7))  # Output: 14
```

This script uses dynamic programming to efficiently compute the n-th element of the Fib4 number sequence. It initializes a list to store the first 4 elements of the sequence and then uses a loop to compute the rest of the sequence. This approach avoids the overhead of recursive function calls and is more memory-efficient than recursion for large values of n.