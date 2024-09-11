```python
def fibfib(n: int) -> int:
    """
    The FibFib number sequence is a sequence similar to the Fibonacci sequence that's defined as follows:
    fibfib(0) == 0
    fibfib(1) == 0
    fibfib(2) == 1
    fibfib(n) == fibfib(n-1) + fibfib(n-2) + fibfib(n-3).
    
    This function efficiently computes the n-th element of the FibFib number sequence.
    """
    
    # Base cases
    if n == 0:
        return 0
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    
    # Initialize variables to store the last three numbers in the sequence
    a, b, c = 0, 0, 1
    
    # Calculate the nth number in the sequence
    for _ in range(3, n + 1):
        a, b, c = b, c, b + c + a
    
    # Return the nth number in the sequence
    return c

# Test the function
print(fibfib(1))  # Should print: 0
print(fibfib(5))  # Should print: 4
print(fibfib(8))  # Should print: 24
```

This script implements the `fibfib` function, which efficiently computes the n-th element of the FibFib number sequence using memoization. The script also includes test cases to verify the correctness of the function.