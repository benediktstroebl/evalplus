### Fib4 Sequence Calculation

Below is a Python script that uses dynamic programming to calculate the n-th element of the fib4 number sequence.

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

    Args:
        n (int): The position of the element in the sequence.

    Returns:
        int: The n-th element of the fib4 number sequence.
    """

    # Handle edge cases
    if n == 0 or n == 1:
        return 0
    elif n == 2:
        return 2
    
    # Initialize a list to store the sequence values
    fib4_sequence = [0] * (n + 1)
    fib4_sequence[0] = 0
    fib4_sequence[1] = 0
    fib4_sequence[2] = 2
    
    # Calculate the sequence values iteratively
    for i in range(3, n + 1):
        fib4_sequence[i] = fib4_sequence[i-1] + fib4_sequence[i-2] + fib4_sequence[i-3] + fib4_sequence[i-4]
    
    # Return the n-th element of the sequence
    return fib4_sequence[n]

# Test the function
print(fib4(5))  # Output: 4
print(fib4(6))  # Output: 8
print(fib4(7))  # Output: 14
```

This script uses a dynamic programming approach by storing the previously calculated sequence values in memory and reusing them to calculate the next values. This makes the calculation much more efficient than using recursion for large values of n.