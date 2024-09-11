```python
def fib4(n: int):
    """
    The Fib4 number sequence is a sequence similar to the Fibonacci sequence 
    that's defined as follows:
    fib4(0) -> 0
    fib4(1) -> 0
    fib4(2) -> 2
    fib4(3) -> 0
    fib4(n) -> fib4(n-1) + fib4(n-2) + fib4(n-3) + fib4(n-4).

    Args:
        n (int): The index of the element in the sequence.

    Returns:
        int: The nth element of the Fib4 number sequence.

    Raises:
        ValueError: If n is a negative integer.
    """
    if n < 0:
        raise ValueError("Input should be a non-negative integer.")

    # Initialize the base cases
    if n == 0 or n == 1:
        return 0
    elif n == 2:
        return 2
    elif n == 3:
        return 0

    # Initialize an array to store the sequence
    fib4_sequence = [0, 0, 2, 0]

    # Compute the sequence up to the nth element
    for i in range(4, n + 1):
        fib4_sequence.append(fib4_sequence[i-1] + fib4_sequence[i-2] + fib4_sequence[i-3] + fib4_sequence[i-4])

    return fib4_sequence[n]

# Test the function
print(fib4(5))   # Output: 4
print(fib4(6))   # Output: 8
print(fib4(7))   # Output: 14
```

This Python script implements the `fib4` function, which efficiently computes the nth element of the Fib4 number sequence using an iterative approach. It initializes the base cases and then uses a loop to compute the sequence up to the nth element, storing it in an array.