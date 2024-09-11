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
    It uses dynamic programming to store the results of previously computed elements.
    
    Args:
    n (int): The position of the element in the fib4 sequence.
    
    Returns:
    int: The n-th element of the fib4 sequence.
    """
    
    # Handle edge cases where n is less than 0
    if n < 0:
        raise ValueError("n must be a non-negative integer")
    
    # Handle base cases where n is 0, 1, 2, or 3
    if n == 0 or n == 1:
        return 0
    elif n == 2:
        return 2
    elif n == 3:
        return 0
    
    # Create a list to store the results of previously computed elements
    fib4_sequence = [0, 0, 2, 0]
    
    # Compute the n-th element of the fib4 sequence
    for i in range(4, n + 1):
        # Use the recurrence relation to compute the next element
        next_element = fib4_sequence[i - 1] + fib4_sequence[i - 2] + fib4_sequence[i - 3] + fib4_sequence[i - 4]
        # Append the next element to the list
        fib4_sequence.append(next_element)
    
    # Return the n-th element of the fib4 sequence
    return fib4_sequence[n]

# Test the function
print(fib4(5))  # Output: 4
print(fib4(6))  # Output: 8
print(fib4(7))  # Output: 14
```

This script uses dynamic programming to efficiently compute the n-th element of the fib4 sequence. It stores the results of previously computed elements in a list, and uses the recurrence relation to compute the next element in each iteration. This approach avoids the overhead of recursive function calls and makes the computation much faster for large values of n.