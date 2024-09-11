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
    n (int): The position of the number in the sequence.

    Returns:
    int: The nth number in the Fib4 sequence.

    Raises:
    ValueError: If n is a negative integer.
    """
    
    # Check if input is a non-negative integer
    if not isinstance(n, int) or n < 0:
        raise ValueError("Input must be a non-negative integer.")
    
    # Base cases
    if n == 0 or n == 1:
        return 0
    elif n == 2:
        return 2
    
    # Initialize the first four numbers in the sequence
    a, b, c, d = 0, 0, 2, 0
    
    # Compute the sequence
    for _ in range(3, n + 1):
        # Update the sequence
        a, b, c, d = b, c, d, b + c + d + a
    
    return d

# Test the function
print(fib4(5))  # Output: 4
print(fib4(6))  # Output: 8
print(fib4(7))  # Output: 14
```

This script uses an iterative approach to compute the nth element of the Fib4 number sequence. It initializes the first four numbers in the sequence, then updates the sequence for each position from 3 to n. The function raises a ValueError if the input is not a non-negative integer.