```python
def fibfib(n: int):
    """
    The FibFib number sequence is a sequence similar to the Fibonacci sequence that's defined as follows:
    fibfib(0) == 0
    fibfib(1) == 0
    fibfib(2) == 1
    fibfib(n) == fibfib(n-1) + fibfib(n-2) + fibfib(n-3).
    
    Args:
    n (int): The index of the FibFib number to compute.
    
    Returns:
    int: The n-th element of the FibFib number sequence.
    """
    if n <= 1:
        return 0
    elif n == 2:
        return 1
    else:
        # Initialize a list to store the first three elements of the sequence
        fibfib_sequence = [0, 0, 1]
        
        # Compute the sequence up to the nth element
        for i in range(3, n + 1):
            next_element = fibfib_sequence[i-1] + fibfib_sequence[i-2] + fibfib_sequence[i-3]
            fibfib_sequence.append(next_element)
        
        # Return the nth element of the sequence
        return fibfib_sequence[n]

# Test cases
print(fibfib(1))   # Output: 0
print(fibfib(5))   # Output: 4
print(fibfib(8))   # Output: 24
```

This script uses dynamic programming to efficiently compute the nth element of the FibFib number sequence. It initializes a list to store the first three elements of the sequence and then iteratively computes the next elements up to the nth element. The time complexity of this algorithm is O(n), making it efficient for large values of n.