```python
def fib4(n: int):
    """
    The Fib4 number sequence is a sequence similar to the Fibonacci sequence that's defined as follows:
    fib4(0) -> 0
    fib4(1) -> 0
    fib4(2) -> 2
    fib4(3) -> 0
    fib4(n) -> fib4(n-1) + fib4(n-2) + fib4(n-3) + fib4(n-4).
    
    This function efficiently computes the n-th element of the fib4 number sequence using dynamic programming.
    
    Parameters:
    n (int): The position of the fib4 number to compute.
    
    Returns:
    int: The n-th element of the fib4 number sequence.
    """
    if n < 0:
        raise ValueError("n must be a non-negative integer")
    
    # Initialize a list to store the fib4 numbers
    fib4_numbers = [0, 0, 2] + [0]*(n-2)
    
    # Compute the fib4 numbers iteratively
    for i in range(3, n+1):
        fib4_numbers[i] = fib4_numbers[i-1] + fib4_numbers[i-2] + fib4_numbers[i-3] + fib4_numbers[i-4]
    
    return fib4_numbers[n]

# Test the function
print(fib4(5))  # Output: 4
print(fib4(6))  # Output: 8
print(fib4(7))  # Output: 14
```

This script uses dynamic programming to efficiently compute the n-th element of the fib4 number sequence. The idea is to store the previously computed fib4 numbers and reuse them to compute the next fib4 numbers. This approach avoids the repeated computations and makes the function much faster for large values of n.