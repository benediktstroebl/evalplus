```python
def fib4(n: int):
    """
    The Fib4 number sequence is a sequence similar to the Fibonacci sequence that's defined as follows:
    fib4(0) -> 0
    fib4(1) -> 0
    fib4(2) -> 2
    fib4(3) -> 0
    fib4(n) -> fib4(n-1) + fib4(n-2) + fib4(n-3) + fib4(n-4).
    
    This function efficiently computes the n-th element of the fib4 number sequence without using recursion.
    
    Parameters:
    n (int): The position of the element in the fib4 sequence.
    
    Returns:
    int: The n-th element of the fib4 sequence.
    """
    if n == 0 or n == 1:
        return 0
    elif n == 2:
        return 2
    elif n == 3:
        return 0

    # Create a list to store the fib4 numbers
    fib4_sequence = [0] * (n + 1)
    fib4_sequence[0] = 0
    fib4_sequence[1] = 0
    fib4_sequence[2] = 2
    fib4_sequence[3] = 0

    # Fill in the rest of the sequence
    for i in range(4, n + 1):
        # fib4(i) = fib4(i-1) + fib4(i-2) + fib4(i-3) + fib4(i-4)
        fib4_sequence[i] = fib4_sequence[i-1] + fib4_sequence[i-2] + fib4_sequence[i-3] + fib4_sequence[i-4]

    return fib4_sequence[n]

# Test the function
print(fib4(5))  # Output: 4
print(fib4(6))  # Output: 8
print(fib4(7))  # Output: 14
```

This script creates a list to store the fib4 numbers as it calculates them, avoiding the need for unnecessary recalculations and improving efficiency.