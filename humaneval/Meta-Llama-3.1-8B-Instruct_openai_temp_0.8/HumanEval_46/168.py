### Efficiently Computing the N-th Element of the Fib4 Number Sequence
```python
def fib4(n: int):
    """
    The Fib4 number sequence is a sequence similar to the Fibbonacci sequence 
    that's defined as follows:
    fib4(0) -> 0
    fib4(1) -> 0
    fib4(2) -> 2
    fib4(3) -> 0
    fib4(n) -> fib4(n-1) + fib4(n-2) + fib4(n-3) + fib4(n-4).
    
    This function efficiently computes the n-th element of the fib4 number sequence.
    
    Args:
    n (int): The index of the element to compute in the fib4 sequence.
    
    Returns:
    int: The n-th element of the fib4 number sequence.
    """
    
    # Handle edge cases
    if n == 0:
        return 0
    elif n == 1:
        return 0
    elif n == 2:
        return 2
    elif n == 3:
        return 0
    
    # Initialize variables to store the last 4 elements
    a, b, c, d = 0, 0, 2, 0
    
    # Iterate from 4 to n (inclusive)
    for _ in range(4, n + 1):
        # Compute the next element as the sum of the last 4 elements
        a, b, c, d = b, c, d, a + b + c + d
    
    # Return the n-th element
    return d

# Test cases
print(fib4(5))  # 4
print(fib4(6))  # 8
print(fib4(7))  # 14
```
This script defines a function `fib4(n)` that efficiently computes the n-th element of the fib4 number sequence. The function uses an iterative approach to store the last 4 elements of the sequence, which allows it to compute the next element as the sum of the last 4 elements. The function handles edge cases and returns the n-th element of the fib4 number sequence.