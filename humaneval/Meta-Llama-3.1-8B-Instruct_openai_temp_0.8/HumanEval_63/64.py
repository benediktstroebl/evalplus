```python
def fibfib(n: int) -> int:
    """
    Compute the n-th element of the FibFib number sequence.
    
    The FibFib number sequence is a sequence similar to the Fibonacci sequence that's defined as follows:
    fibfib(0) == 0
    fibfib(1) == 0
    fibfib(2) == 1
    fibfib(n) == fibfib(n-1) + fibfib(n-2) + fibfib(n-3).
    
    Args:
        n (int): The index of the element to compute.
    
    Returns:
        int: The n-th element of the FibFib number sequence.
    """
    
    # Base cases
    if n == 0 or n == 1:
        return 0
    
    # Initialize a list to store the computed values
    fibfib_values = [0, 0, 1]
    
    # Compute the values from 3 to n
    for i in range(3, n + 1):
        # Compute the next value as the sum of the previous three values
        next_value = fibfib_values[i - 1] + fibfib_values[i - 2] + fibfib_values[i - 3]
        # Append the next value to the list
        fibfib_values.append(next_value)
    
    # Return the n-th value
    return fibfib_values[n]

# Test the function
print(fibfib(1))  # 0
print(fibfib(5))  # 4
print(fibfib(8))  # 24
```

However, the above script has a time complexity of O(n), which can become inefficient for large values of n.

Here's a more efficient version of the script, with a time complexity of O(n), but with a constant factor of 2, using a technique called memoization:

```python
def fibfib(n: int) -> int:
    """
    Compute the n-th element of the FibFib number sequence.
    
    The FibFib number sequence is a sequence similar to the Fibonacci sequence that's defined as follows:
    fibfib(0) == 0
    fibfib(1) == 0
    fibfib(2) == 1
    fibfib(n) == fibfib(n-1) + fibfib(n-2) + fibfib(n-3).
    
    Args:
        n (int): The index of the element to compute.
    
    Returns:
        int: The n-th element of the FibFib number sequence.
    """
    
    # Base cases
    if n == 0 or n == 1:
        return 0
    
    # Initialize a dictionary to store the computed values
    memo = {0: 0, 1: 0, 2: 1}
    
    # Compute the values from 3 to n
    for i in range(3, n + 1):
        # Compute the next value as the sum of the previous three values
        if i not in memo:
            memo[i] = memo[i - 1] + memo[i - 2] + memo[i - 3]
    
    # Return the n-th value
    return memo[n]

# Test the function
print(fibfib(1))  # 0
print(fibfib(5))  # 4
print(fibfib(8))  # 24
```

This version of the script will also work for large values of n, but it will use more memory.