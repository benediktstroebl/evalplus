```python
def fibfib(n: int) -> int:
    """
    The FibFib number sequence is a sequence similar to the Fibbonacci sequence 
    that's defined as follows:
    fibfib(0) == 0
    fibfib(1) == 0
    fibfib(2) == 1
    fibfib(n) == fibfib(n-1) + fibfib(n-2) + fibfib(n-3).
    
    Args:
        n (int): The index of the FibFib number to compute.
    
    Returns:
        int: The n-th element of the FibFib number sequence.
    """
    
    # Base cases
    if n == 0:
        return 0
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    
    # Create a list to store the Fibonacci sequence
    fib_sequence = [0, 0, 1]
    
    # Compute the Fibonacci sequence up to the n-th element
    for i in range(3, n + 1):
        # Compute the next element as the sum of the previous three elements
        next_element = fib_sequence[i - 1] + fib_sequence[i - 2] + fib_sequence[i - 3]
        fib_sequence.append(next_element)
    
    # Return the n-th element
    return fib_sequence[n]


# Test cases
print(fibfib(1))  # Expected output: 0
print(fibfib(5))  # Expected output: 4
print(fibfib(8))  # Expected output: 24
```

This script uses dynamic programming to efficiently compute the n-th element of the FibFib number sequence. It first checks for base cases and then uses a list to store the Fibonacci sequence up to the n-th element. The next element is computed as the sum of the previous three elements, and it is appended to the list. Finally, the n-th element is returned.