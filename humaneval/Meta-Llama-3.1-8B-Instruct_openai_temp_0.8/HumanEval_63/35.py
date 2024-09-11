```python
def fibfib(n: int) -> int:
    """
    Compute the n-th element of the FibFib number sequence.
    
    The FibFib number sequence is a sequence similar to the Fibonacci sequence that's defined as follows:
    fibfib(0) == 0
    fibfib(1) == 0
    fibfib(2) == 1
    fibfib(n) == fibfib(n-1) + fibfib(n-2) + fibfib(n-3).
    
    Args:
        n (int): The index of the element to compute.
        
    Returns:
        int: The n-th element of the FibFib number sequence.
    """
    if n <= 0:
        return 0
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        # Initialize a list to store the Fibonacci sequence
        fibfib_sequence = [0, 0, 1]
        
        # Compute the first 3 elements of the sequence
        for i in range(3, n + 1):
            # Use dynamic programming to compute the next element
            fibfib_sequence.append(fibfib_sequence[i - 1] + fibfib_sequence[i - 2] + fibfib_sequence[i - 3])
        
        # Return the n-th element of the sequence
        return fibfib_sequence[n]


# Test the function
print(fibfib(1))  # Output: 0
print(fibfib(5))  # Output: 4
print(fibfib(8))  # Output: 24
```