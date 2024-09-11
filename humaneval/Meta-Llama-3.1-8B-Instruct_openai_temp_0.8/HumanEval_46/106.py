```python
def fib4(n: int):
    """
    The Fib4 number sequence is a sequence similar to the Fibbonacci sequence that's defined as follows:
    fib4(0) -> 0
    fib4(1) -> 0
    fib4(2) -> 2
    fib4(3) -> 0
    fib4(n) -> fib4(n-1) + fib4(n-2) + fib4(n-3) + fib4(n-4).

    This function efficiently computes the n-th element of the fib4 number sequence using dynamic programming.

    Args:
        n (int): The position of the element in the fib4 sequence.

    Returns:
        int: The n-th element of the fib4 sequence.
    """
    if n <= 1:
        return 0
    elif n == 2:
        return 2
    elif n == 3:
        return 0

    # Initialize a list to store the fib4 sequence up to the n-th element
    fib4_sequence = [0, 0, 2, 0]

    # Iterate from 4 to n (inclusive) to fill up the fib4_sequence list
    for i in range(4, n + 1):
        # The i-th element is the sum of the previous 4 elements
        fib4_sequence.append(fib4_sequence[i - 1] + fib4_sequence[i - 2] + fib4_sequence[i - 3] + fib4_sequence[i - 4])

    # Return the n-th element of the fib4 sequence
    return fib4_sequence[n]


# Test cases
print(fib4(5))  # Output: 4
print(fib4(6))  # Output: 8
print(fib4(7))  # Output: 14
```

This script defines a function `fib4(n)` that efficiently computes the n-th element of the fib4 number sequence using dynamic programming. It initializes a list to store the fib4 sequence up to the n-th element and then fills up the list by iterating from 4 to n (inclusive). The i-th element is calculated as the sum of the previous 4 elements. Finally, the function returns the n-th element of the fib4 sequence. The test cases demonstrate the correctness of the function.