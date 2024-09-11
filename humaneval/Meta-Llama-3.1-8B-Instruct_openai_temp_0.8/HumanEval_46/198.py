### Efficiently Computing the Fib4 Number Sequence in Python
```python
def fib4(n: int) -> int:
    """
    This function efficiently computes the n-th element of the Fib4 number sequence.
    
    The Fib4 number sequence is defined as follows:
    fib4(0) -> 0
    fib4(1) -> 0
    fib4(2) -> 2
    fib4(3) -> 0
    fib4(n) -> fib4(n-1) + fib4(n-2) + fib4(n-3) + fib4(n-4).
    
    Parameters:
    n (int): The index of the element in the Fib4 number sequence.
    
    Returns:
    int: The n-th element of the Fib4 number sequence.
    """
    
    # Handle edge cases where n is less than 2
    if n == 0 or n == 1:
        return 0
    elif n == 2:
        return 2
    elif n == 3:
        return 0
    
    # Initialize an array to store the Fibonacci numbers
    fib4_sequence = [0] * (n + 1)
    
    # Base cases
    fib4_sequence[0] = 0
    fib4_sequence[1] = 0
    fib4_sequence[2] = 2
    fib4_sequence[3] = 0
    
    # Compute the Fib4 numbers iteratively
    for i in range(4, n + 1):
        fib4_sequence[i] = fib4_sequence[i - 1] + fib4_sequence[i - 2] + fib4_sequence[i - 3] + fib4_sequence[i - 4]
    
    # Return the n-th element of the Fib4 number sequence
    return fib4_sequence[n]

# Test the function
print(fib4(5))  # Output: 4
print(fib4(6))  # Output: 8
print(fib4(7))  # Output: 14
```
This script uses dynamic programming to efficiently compute the n-th element of the Fib4 number sequence. It initializes an array to store the Fibonacci numbers and then computes them iteratively, avoiding recursion. The function handles edge cases and returns the n-th element of the sequence.