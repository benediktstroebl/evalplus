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
        n (int): The index of the element in the fibfib sequence.
    
    Returns:
        int: The n-th element of the fibfib sequence.
    """
    # Initialize a dictionary to store previously computed values
    memo = {0: 0, 1: 0, 2: 1}
    
    # Define a helper function to perform the recursive computation
    def fibfib_helper(k: int) -> int:
        # If the value has already been computed, return it directly
        if k in memo:
            return memo[k]
        
        # Otherwise, compute the value and store it in the memo dictionary
        else:
            result = fibfib_helper(k-1) + fibfib_helper(k-2) + fibfib_helper(k-3)
            memo[k] = result
            return result
    
    # If n is in the memo dictionary, return its value directly
    if n in memo:
        return memo[n]
    
    # Otherwise, compute the value using the helper function and return it
    else:
        return fibfib_helper(n)


# Test the function
print(fibfib(1))  # Output: 0
print(fibfib(5))  # Output: 4
print(fibfib(8))  # Output: 24
```

This script defines a function `fibfib` that computes the n-th element of the FibFib number sequence using memoization. It uses a dictionary `memo` to store previously computed values and a helper function `fibfib_helper` to perform the recursive computation. This approach minimizes repeated computation and reduces the time complexity of the function.