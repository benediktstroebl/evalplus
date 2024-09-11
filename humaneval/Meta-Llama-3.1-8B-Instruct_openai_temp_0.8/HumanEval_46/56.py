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
        n (int): The position of the number in the Fib4 sequence.

    Returns:
        int: The nth number in the Fib4 sequence.
    """
    if n < 0:
        raise ValueError("n must be a non-negative integer")
    
    # Initialize the first four numbers in the sequence
    a, b, c, d = 0, 0, 2, 0
    
    # Loop from 4 to n (inclusive)
    for _ in range(4, n + 1):
        # Calculate the next number as the sum of the last four numbers
        a, b, c, d = b, c, d, a + b + c + d
    
    # Return the nth number in the sequence
    return d

# Test the function
print(fib4(5))   # 4
print(fib4(6))   # 8
print(fib4(7))   # 14
```

This script uses a loop to efficiently compute the nth number in the Fib4 sequence. It starts with the first four numbers in the sequence (0, 0, 2, and 0) and then iteratively calculates the next numbers as the sum of the last four numbers. This approach avoids the overhead of recursion and is more efficient for large values of n.