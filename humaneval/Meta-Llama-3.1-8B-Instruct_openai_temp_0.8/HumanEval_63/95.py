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
    int: The nth number in the sequence.
    """
    
    # Initialize a dictionary to store the computed values
    memo = {0: 0, 1: 0, 2: 1}
    
    def fibfib_helper(k: int) -> int:
        """
        Helper function to compute the value recursively
        """
        
        # If the value is already computed, return it from the memo
        if k in memo:
            return memo[k]
        
        # Otherwise, compute the value and store it in the memo
        else:
            result = fibfib_helper(k-1) + fibfib_helper(k-2) + fibfib_helper(k-3)
            memo[k] = result
            return result
    
    # Call the helper function to compute the nth value
    return fibfib_helper(n)

# Test the function
print(fibfib(1))   # Output: 0
print(fibfib(5))   # Output: 4
print(fibfib(8))   # Output: 24
```

This script uses a technique called memoization, which stores the results of expensive function calls and reuses them when the same inputs occur again. This approach significantly improves the performance of the function for larger inputs.