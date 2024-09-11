```python
def fibfib(n: int) -> int:
    """The FibFib number sequence is a sequence similar to the Fibonacci sequence that's defined as follows:
    fibfib(0) == 0
    fibfib(1) == 0
    fibfib(2) == 1
    fibfib(n) == fibfib(n-1) + fibfib(n-2) + fibfib(n-3).
    
    Args:
        n (int): The index of the fibfib number to compute.
    
    Returns:
        int: The n-th element of the fibfib number sequence.
    
    Raises:
        ValueError: If n is a negative integer.
    """
    if n < 0:
        raise ValueError("n must be a non-negative integer.")
    
    # Base cases
    if n == 0 or n == 1:
        return 0
    elif n == 2:
        return 1
    
    # Create a list to store the fibfib numbers
    fibfib_numbers = [0, 0, 1]
    
    # Compute the fibfib numbers iteratively
    for i in range(3, n + 1):
        # Compute the next fibfib number as the sum of the previous three numbers
        next_fibfib = fibfib_numbers[i - 1] + fibfib_numbers[i - 2] + fibfib_numbers[i - 3]
        # Append the next fibfib number to the list
        fibfib_numbers.append(next_fibfib)
    
    # Return the n-th fibfib number
    return fibfib_numbers[n]


# Test the function
print(fibfib(1))  # Output: 0
print(fibfib(5))  # Output: 4
print(fibfib(8))  # Output: 24
```

However, we can do this efficiently using dynamic programming and memoization for a more optimized solution. Here is how to do it:

```python
def fibfib(n: int) -> int:
    """The FibFib number sequence is a sequence similar to the Fibonacci sequence that's defined as follows:
    fibfib(0) == 0
    fibfib(1) == 0
    fibfib(2) == 1
    fibfib(n) == fibfib(n-1) + fibfib(n-2) + fibfib(n-3).
    
    Args:
        n (int): The index of the fibfib number to compute.
    
    Returns:
        int: The n-th element of the fibfib number sequence.
    
    Raises:
        ValueError: If n is a negative integer.
    """
    if n < 0:
        raise ValueError("n must be a non-negative integer.")
    
    # Create a dictionary to store the memoized fibfib numbers
    memo = {0: 0, 1: 0, 2: 1}
    
    def fibfib_helper(k: int) -> int:
        # If the fibfib number is already memoized, return it
        if k in memo:
            return memo[k]
        # Otherwise, compute the fibfib number and memoize it
        else:
            result = fibfib_helper(k - 1) + fibfib_helper(k - 2) + fibfib_helper(k - 3)
            memo[k] = result
            return result
    
    # Compute and return the n-th fibfib number
    return fibfib_helper(n)


# Test the function
print(fibfib(1))  # Output: 0
print(fibfib(5))  # Output: 4
print(fibfib(8))  #