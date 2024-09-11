```python
def fibfib(n: int) -> int:
    """
    The FibFib number sequence is a sequence similar to the Fibonacci sequence 
    that's defined as follows:
    fibfib(0) == 0
    fibfib(1) == 0
    fibfib(2) == 1
    fibfib(n) == fibfib(n-1) + fibfib(n-2) + fibfib(n-3).
    
    This function efficiently computes the n-th element of the fibfib number sequence.
    
    Parameters:
    n (int): The position of the number in the sequence.
    
    Returns:
    int: The n-th element of the fibfib number sequence.
    """
    if n <= 2:
        return 0
    elif n == 3:
        return 1
    
    # Initialize a list to store the sequence, with the first three elements.
    sequence = [0, 0, 1] + [0]*(n-3)
    
    # Compute the sequence up to the nth element.
    for i in range(4, n+1):
        sequence[i-1] = sequence[i-2] + sequence[i-3] + sequence[i-4]
    
    # Return the nth element of the sequence.
    return sequence[-1]

# Test the function
print(fibfib(1))  # 0
print(fibfib(5))  # 4
print(fibfib(8))  # 24
```

This script defines a function `fibfib(n)` that computes the nth element of the FibFib number sequence. It uses a list `sequence` to store the sequence up to the nth element, and then returns the nth element. The time complexity of this function is O(n), which is efficient for large values of n.