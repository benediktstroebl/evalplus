### Fib4 Number Sequence
#### Efficient Computation using Dynamic Programming

```python
def fib4(n: int) -> int:
    """
    The Fib4 number sequence is a sequence similar to the Fibonacci sequence that's defined as follows:
    fib4(0) -> 0
    fib4(1) -> 0
    fib4(2) -> 2
    fib4(3) -> 0
    fib4(n) -> fib4(n-1) + fib4(n-2) + fib4(n-3) + fib4(n-4).
    
    This function efficiently computes the n-th element of the fib4 number sequence using dynamic programming.
    
    Args:
    n (int): The index of the element in the fib4 sequence.
    
    Returns:
    int: The n-th element of the fib4 sequence.
    """
    
    # Base cases
    if n == 0:
        return 0
    elif n == 1:
        return 0
    elif n == 2:
        return 2
    elif n == 3:
        return 0
    
    # Initialize array to store fib4 values
    fib4_values = [0] * (n + 1)
    fib4_values[0] = 0
    fib4_values[1] = 0
    fib4_values[2] = 2
    fib4_values[3] = 0
    
    # Compute fib4 values iteratively
    for i in range(4, n + 1):
        fib4_values[i] = fib4_values[i-1] + fib4_values[i-2] + fib4_values[i-3] + fib4_values[i-4]
    
    return fib4_values[n]

# Example usage
print(fib4(5))  # Output: 4
print(fib4(6))  # Output: 8
print(fib4(7))  # Output: 14
```

This script defines a function `fib4(n)` that efficiently computes the n-th element of the fib4 number sequence using dynamic programming. The function initializes an array `fib4_values` to store the computed values and then iteratively calculates the fib4 values using the recurrence relation. The base cases are handled separately.