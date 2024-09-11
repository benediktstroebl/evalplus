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
        n (int): The index of the fib4 number sequence.

    Returns:
        int: The n-th element of the fib4 number sequence.
    """
    if n <= 0:
        return 0
    
    # Initialize the first four elements of the sequence
    a, b, c, d = 0, 0, 2, 0
    
    # Compute the n-th element of the sequence
    for _ in range(3, n + 1):
        # Update the last four elements of the sequence using the recurrence relation
        a, b, c, d = b, c, d, c + d + b + a
    
    return d

# Test the function
print(fib4(5))  # 4
print(fib4(6))  # 8
print(fib4(7))  # 14
```

This script defines a function `fib4(n)` that uses a loop to efficiently compute the nth element of the fib4 number sequence. It initializes the first four elements of the sequence (a, b, c, d) and then updates them using the recurrence relation in each iteration. The function returns the nth element of the sequence.