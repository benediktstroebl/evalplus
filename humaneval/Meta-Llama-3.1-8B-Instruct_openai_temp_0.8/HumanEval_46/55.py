```python
def fib4(n: int):
    """
    The Fib4 number sequence is a sequence similar to the Fibonacci sequence that's defined as follows:
    fib4(0) -> 0
    fib4(1) -> 0
    fib4(2) -> 2
    fib4(3) -> 0
    fib4(n) -> fib4(n-1) + fib4(n-2) + fib4(n-3) + fib4(n-4).

    This function efficiently computes the n-th element of the fib4 number sequence without using recursion.
    
    Args:
        n (int): The position of the element in the sequence.

    Returns:
        int: The n-th element of the fib4 number sequence.
    """
    # Base cases
    if n == 0 or n == 1:
        return 0
    elif n == 2:
        return 2
    elif n == 3:
        return 0

    # Initialize a list to store the sequence
    fib4_sequence = [0, 0, 2, 0]
    for i in range(4, n + 1):
        # Compute the i-th element
        fib4_sequence.append(fib4_sequence[i-1] + fib4_sequence[i-2] + fib4_sequence[i-3] + fib4_sequence[i-4])

    # Return the n-th element
    return fib4_sequence[n]


# Test cases
print(fib4(5))  # Output: 4
print(fib4(6))  # Output: 8
print(fib4(7))  # Output: 14
```

This script defines the `fib4` function to compute the n-th element of the fib4 number sequence. It first checks the base cases and then uses a loop to compute the sequence up to the n-th element. The function returns the n-th element of the sequence.

The test cases at the end of the script verify that the `fib4` function produces the correct results for the inputs 5, 6, and 7.