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
    
    This function efficiently computes the n-th element of the fib4 number sequence.
    
    Args:
    n (int): The position of the number in the sequence.
    
    Returns:
    int: The nth number in the fib4 sequence.
    
    Examples:
    >>> fib4(5)
    4
    >>> fib4(6)
    8
    >>> fib4(7)
    14
    """
    # Base case for the sequence
    if n < 3:
        return 0
    
    # Initialize the base of the sequence
    a, b, c, d = 0, 0, 2, 0
    
    # Iterate over the sequence
    for _ in range(3, n + 1):
        # Update the values for the next element
        a, b, c, d = b, c, d, a + b + c + d
    
    # Return the nth element
    return d

# Test the function
print(fib4(5))   # 4
print(fib4(6))   # 8
print(fib4(7))   # 14
```

This script uses an iterative approach to compute the nth element of the fib4 number sequence. It initializes the base of the sequence, then iterates over the sequence to update the values for the next element. The function returns the nth element after the iteration is complete. The time complexity of this approach is O(n), making it efficient for large inputs.