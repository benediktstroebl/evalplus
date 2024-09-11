```python
def fibfib(n: int) -> int:
    """
    The FibFib number sequence is a sequence similar to the Fibonacci sequence that's defined as follows:
    fibfib(0) == 0
    fibfib(1) == 0
    fibfib(2) == 1
    fibfib(n) == fibfib(n-1) + fibfib(n-2) + fibfib(n-3).
    
    This function efficiently computes the n-th element of the fibfib number sequence using memoization.
    
    Args:
        n (int): The index of the element in the fibfib sequence to be computed.
    
    Returns:
        int: The n-th element of the fibfib sequence.
    """
    
    # Base cases
    if n == 0 or n == 1:
        return 0
    elif n == 2:
        return 1
    
    # Initialize memoization dictionary
    memo = {0: 0, 1: 0, 2: 1}
    
    # Compute and store fibfib values in memo dictionary
    for i in range(3, n + 1):
        memo[i] = memo[i-1] + memo[i-2] + memo[i-3]
    
    # Return the computed fibfib value
    return memo[n]

# Test cases
print(fibfib(1))  # Expected output: 0
print(fibfib(5))  # Expected output: 4
print(fibfib(8))  # Expected output: 24
```

This script defines a function `fibfib(n)` that efficiently computes the n-th element of the fibfib sequence using memoization. The function first checks for base cases and then uses a dictionary `memo` to store and look up previously computed fibfib values. This approach significantly reduces the time complexity of the function, making it more efficient for large inputs.