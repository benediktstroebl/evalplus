```python
def fibfib(n: int) -> int:
    """
    The FibFib number sequence is a sequence similar to the Fibonacci sequence that's defined as follows:
    fibfib(0) == 0
    fibfib(1) == 0
    fibfib(2) == 1
    fibfib(n) == fibfib(n-1) + fibfib(n-2) + fibfib(n-3).
    
    Args:
    n (int): The position of the element in the sequence to be computed.
    
    Returns:
    int: The n-th element of the FibFib number sequence.
    """
    
    # Base cases
    if n == 0 or n == 1:
        return 0
    
    # Initialize a list to store the sequence
    fibfib_sequence = [0] * (n + 1)
    
    # Set the first two elements
    fibfib_sequence[0] = 0
    fibfib_sequence[1] = 0
    
    # Compute the first three elements
    if n >= 2:
        fibfib_sequence[2] = 1
    
    # Compute the rest of the sequence
    for i in range(3, n + 1):
        fibfib_sequence[i] = fibfib_sequence[i-1] + fibfib_sequence[i-2] + fibfib_sequence[i-3]
    
    # Return the n-th element
    return fibfib_sequence[n]

# Test cases
print(fibfib(1))  # 0
print(fibfib(5))  # 4
print(fibfib(8))  # 24
```

This script defines a function `fibfib(n)` to compute the n-th element of the FibFib number sequence. The function uses dynamic programming to efficiently compute the sequence. It first initializes a list to store the sequence, then sets the first two elements, and finally computes the rest of the sequence using a loop. The function returns the n-th element of the sequence. The test cases at the end verify that the function works correctly.