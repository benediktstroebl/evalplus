```python
# We will use memoization to store the values of the fibfib sequence as we compute them
# This will avoid redundant computations and make the function much more efficient
def fibfib(n: int, memo={}):
    """
    Compute the n-th element of the FibFib number sequence.
    
    The FibFib number sequence is defined as follows:
    fibfib(0) == 0
    fibfib(1) == 0
    fibfib(2) == 1
    fibfib(n) == fibfib(n-1) + fibfib(n-2) + fibfib(n-3)
    
    Args:
        n (int): The index of the element to compute.
        memo (dict): A dictionary to store the memoized values. Defaults to an empty dictionary.
    
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
    
    # If the value is already memoized, return it
    if n in memo:
        return memo[n]
    
    # Otherwise, compute the value and store it in the memo dictionary
    memo[n] = fibfib(n-1, memo) + fibfib(n-2, memo) + fibfib(n-3, memo)
    
    return memo[n]

# Test the function
print(fibfib(1))  # Output: 0
print(fibfib(5))  # Output: 4
print(fibfib(8))  # Output: 24
```

This script defines a function `fibfib` that uses memoization to compute the n-th element of the FibFib number sequence. The function takes an optional `memo` dictionary as an argument, which is used to store the memoized values. The function first checks for base cases, then checks if the value is already memoized. If it is, the function returns the memoized value. Otherwise, the function computes the value, stores it in the memo dictionary, and returns it.

The function is tested with the provided example use cases.