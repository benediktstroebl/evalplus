```python
def fibfib(n: int) -> int:
    """
    Compute the n-th element of the FibFib number sequence.
    
    The FibFib number sequence is a sequence similar to the Fibonacci sequence, 
    defined as follows: 
    fibfib(0) == 0, 
    fibfib(1) == 0, 
    fibfib(2) == 1, 
    fibfib(n) == fibfib(n-1) + fibfib(n-2) + fibfib(n-3).
    
    Args:
        n: The position of the element in the sequence.
    
    Returns:
        The n-th element of the FibFib number sequence.
    """
    if n <= 1:  # Base case
        return 0
    elif n == 2:  # Base case
        return 1
    elif n == 3:  # Base case
        return 1
    elif n == 4:  # Base case
        return 4
    else:  # Recursive case
        return fibfib(n-1) + fibfib(n-2) + fibfib(n-3)


# Test cases
print(fibfib(1))  # Expected output: 0
print(fibfib(5))  # Expected output: 4
print(fibfib(8))  # Expected output: 24
```

However, the above code uses a lot of repeated calculations which makes it inefficient for large values of `n`. A better approach would be to use dynamic programming to store the results of previously computed values.

Here's a more efficient version of the function:

```python
def fibfib(n: int) -> int:
    """
    Compute the n-th element of the FibFib number sequence.
    
    The FibFib number sequence is a sequence similar to the Fibonacci sequence, 
    defined as follows: 
    fibfib(0) == 0, 
    fibfib(1) == 0, 
    fibfib(2) == 1, 
    fibfib(n) == fibfib(n-1) + fibfib(n-2) + fibfib(n-3).
    
    Args:
        n: The position of the element in the sequence.
    
    Returns:
        The n-th element of the FibFib number sequence.
    """
    if n <= 1:  # Base case
        return 0
    elif n == 2:  # Base case
        return 1
    elif n == 3:  # Base case
        return 1
    elif n == 4:  # Base case
        return 4
    
    dp = [0] * (n + 1)  # Create a list to store the results of previously computed values
    dp[2] = 1
    dp[3] = 1
    dp[4] = 4
    
    for i in range(5, n + 1):  # Compute the values from 5 to n
        dp[i] = dp[i-1] + dp[i-2] + dp[i-3]
    
    return dp[n]  # Return the n-th element


# Test cases
print(fibfib(1))  # Expected output: 0
print(fibfib(5))  # Expected output: 4
print(fibfib(8))  # Expected output: 24
```

This code has a time complexity of O(n) and a space complexity of O(n), which is much more efficient than the original recursive code for large values of `n`.