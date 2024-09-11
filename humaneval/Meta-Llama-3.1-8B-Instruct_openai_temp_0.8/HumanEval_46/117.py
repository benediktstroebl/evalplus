### Fib4 Number Sequence
#### Efficient Computation using Dynamic Programming

Here's a Python function that uses dynamic programming to efficiently compute the n-th element of the Fib4 number sequence.

```python
def fib4(n: int):
    """
    The Fib4 number sequence is a sequence similar to the Fibbonacci sequence that's defined as follows:
    fib4(0) -> 0
    fib4(1) -> 0
    fib4(2) -> 2
    fib4(3) -> 0
    fib4(n) -> fib4(n-1) + fib4(n-2) + fib4(n-3) + fib4(n-4).
    
    Args:
    n (int): The index of the Fib4 number to compute.
    
    Returns:
    int: The n-th element of the Fib4 number sequence.
    """
    
    # Base cases
    if n == 0 or n == 1:
        return 0
    elif n == 2:
        return 2
    
    # Initialize the first four elements
    a, b, c, d = 0, 0, 2, 0
    
    # Compute the remaining elements using dynamic programming
    for _ in range(3, n + 1):
        a, b, c, d = b, c, d, a + b + c + d
    
    return d

# Test cases
print(fib4(5))  # Expected output: 4
print(fib4(6))  # Expected output: 8
print(fib4(7))  # Expected output: 14
```

This script uses a loop to iteratively compute the n-th element of the Fib4 number sequence, avoiding recursion to improve performance.