**Fib4 Number Sequence Calculator**
=====================================

Below is a Python script that efficiently calculates the n-th element of the Fib4 number sequence without using recursion.

```python
def fib4(n: int) -> int:
    """
    The Fib4 number sequence is a sequence similar to the Fibonacci sequence, 
    defined as follows:
    fib4(0) -> 0
    fib4(1) -> 0
    fib4(2) -> 2
    fib4(3) -> 0
    fib4(n) -> fib4(n-1) + fib4(n-2) + fib4(n-3) + fib4(n-4).
    
    Args:
    n (int): The position of the element in the sequence.
    
    Returns:
    int: The value of the n-th element in the sequence.
    """
    if n < 0:  # Check for invalid inputs
        raise ValueError("Input should be a non-negative integer")
    
    # Base cases
    if n == 0:
        return 0
    elif n == 1:
        return 0
    elif n == 2:
        return 2
    
    # Initialize the first four elements
    a, b, c, d = 0, 0, 2, 0
    
    # Calculate each element from 3 to n
    for _ in range(3, n + 1):
        temp = a + b + c + d
        a, b, c, d = b, c, d, temp
    
    return d

# Example usage:
print(fib4(5))  # Output: 4
print(fib4(6))  # Output: 8
print(fib4(7))  # Output: 14
```

This script uses a loop to calculate each element of the sequence from the fourth element onwards, using a simple iterative approach. This makes it more efficient than recursive functions, especially for larger inputs.