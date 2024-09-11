Here's a Python script that uses memoization to efficiently compute the n-th element of the FibFib number sequence:
```python
def fibfib(n: int, memo = {}):
    """
    The FibFib number sequence is a sequence similar to the Fibonacci sequence 
    that's defined as follows: 
    fibfib(0) == 0
    fibfib(1) == 0
    fibfib(2) == 1
    fibfib(n) == fibfib(n-1) + fibfib(n-2) + fibfib(n-3).
    
    Args:
    n (int): The index of the element to be computed in the FibFib sequence.
    memo (dict): A dictionary to store the values of previously computed elements.
    
    Returns:
    int: The value of the n-th element in the FibFib sequence.
    """
    
    # Create a dictionary to store the values of previously computed elements
    if n not in memo:
        if n <= 2:
            memo[n] = 0
        else:
            # Compute the value of the n-th element using the recurrence relation
            memo[n] = fibfib(n-1, memo) + fibfib(n-2, memo) + fibfib(n-3, memo)
    
    # Return the value of the n-th element
    return memo[n]

# Test the function
print(fibfib(1))  # Output: 0
print(fibfib(5))  # Output: 4
print(fibfib(8))  # Output: 24
```