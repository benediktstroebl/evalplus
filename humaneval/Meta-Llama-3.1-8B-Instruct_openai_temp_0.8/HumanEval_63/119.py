```python
def fibfib(n: int):
    """
    The FibFib number sequence is a sequence similar to the Fibonacci sequence 
    that's defined as follows:
    fibfib(0) == 0
    fibfib(1) == 0
    fibfib(2) == 1
    fibfib(n) == fibfib(n-1) + fibfib(n-2) + fibfib(n-3).
    
    This function efficiently computes the n-th element of the fibfib number sequence.
    """
    if n <= 2:  # Base cases
        return 0 if n == 1 else 1
    
    # Initialize the dynamic programming array with base cases
    dp = [0] * (n + 1)
    dp[1] = 0
    dp[2] = 1
    
    # Fill the dp array using the recursive relationship
    for i in range(3, n + 1):
        dp[i] = dp[i-1] + dp[i-2] + dp[i-3]
    
    return dp[n]

# Test cases
print(fibfib(1))  # Output: 0
print(fibfib(5))  # Output: 4
print(fibfib(8))  # Output: 24
```

Note that we use dynamic programming to store the results of the previously computed terms to efficiently compute the nth term of the fibfib number sequence. The time complexity of this solution is O(n), which is much more efficient than the naive recursive approach, which would have a time complexity of O(3^n) due to the repeated computation of the same subproblems.