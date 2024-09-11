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
    n (int): The position of the element in the FibFib sequence.

    Returns:
    int: The nth element of the FibFib sequence.

    Raises:
    ValueError: If n is less than 0.
    """
    if n < 0:
        raise ValueError("n must be a non-negative integer.")
    
    # Handle base cases
    if n == 0:
        return 0
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    
    # Create a dictionary to store the computed values
    # This will help us avoid redundant computation
    fibfib_dict = {0: 0, 1: 0, 2: 1}
    
    # Compute the values iteratively
    for i in range(3, n + 1):
        fibfib_dict[i] = fibfib_dict[i-1] + fibfib_dict[i-2] + fibfib_dict[i-3]
    
    return fibfib_dict[n]

# Test the function
print(fibfib(1))   # Output: 0
print(fibfib(5))   # Output: 4
print(fibfib(8))   # Output: 24
```

This script uses a dictionary to store the computed values of the FibFib sequence. It starts by initializing the dictionary with the base cases (n = 0, 1, 2), and then iteratively computes the values for n = 3 to n (inclusive). The function then returns the value of the dictionary for the given n. This approach avoids redundant computation and makes the function more efficient.