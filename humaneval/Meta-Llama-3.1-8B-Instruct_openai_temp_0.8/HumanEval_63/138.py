```python
def fibfib(n: int) -> int:
    """
    The FibFib number sequence is a sequence similar to the Fibonacci sequence 
    that's defined as follows:
    fibfib(0) == 0
    fibfib(1) == 0
    fibfib(2) == 1
    fibfib(n) == fibfib(n-1) + fibfib(n-2) + fibfib(n-3).
    
    Args:
        n (int): The position of the number in the sequence.
    
    Returns:
        int: The nth number in the FibFib sequence.
    """
    if n <= 1:
        return 0
    elif n == 2:
        return 1
    elif n <= 3:
        return 0
    else:
        # Initialize a list to store the computed values
        fibfib_values = [0, 0, 1] + [0]*(n-3)
        
        # Compute the values iteratively
        for i in range(3, n+1):
            fibfib_values[i] = fibfib_values[i-1] + fibfib_values[i-2] + fibfib_values[i-3]
        
        return fibfib_values[n]


# Example usage
print(fibfib(1))  # Output: 0
print(fibfib(5))  # Output: 4
print(fibfib(8))  # Output: 24
```

This script uses dynamic programming to compute the nth number in the FibFib sequence. It initializes a list to store the computed values, then iterates over the range from 3 to n, computing each value based on the previous three values. The function returns the nth value in the list.