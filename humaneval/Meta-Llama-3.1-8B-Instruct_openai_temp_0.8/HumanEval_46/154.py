### Fibonacci-like Sequence: Fib4 Number Sequence

Below is a Python script that calculates the n-th element of the Fib4 number sequence.

```python
def fib4(n: int) -> int:
    """
    Compute the n-th element of the Fib4 number sequence.
    
    The Fib4 number sequence is a sequence similar to the Fibonacci sequence 
    that's defined as follows:
    fib4(0) -> 0
    fib4(1) -> 0
    fib4(2) -> 2
    fib4(3) -> 0
    fib4(n) -> fib4(n-1) + fib4(n-2) + fib4(n-3) + fib4(n-4).
    
    Args:
        n (int): The position of the element in the Fib4 sequence.
    
    Returns:
        int: The n-th element of the Fib4 sequence.
    """
    if n < 4:
        # Base cases for the sequence
        return [0, 0, 2, 0][n]
    
    # Initialize the first four elements of the sequence
    a, b, c, d = 0, 0, 2, 0
    
    # Iterate from 4 to n
    for _ in range(4, n + 1):
        # Compute the next element as the sum of the last four elements
        a, b, c, d = b, c, d, a + b + c + d
    
    # Return the n-th element
    return d


# Example usage
print(fib4(5))   # Output: 4
print(fib4(6))   # Output: 8
print(fib4(7))   # Output: 14
```

This script uses an iterative approach to calculate the n-th element of the Fib4 sequence. It maintains a running list of the last four elements and updates them in each iteration to compute the next element in the sequence.