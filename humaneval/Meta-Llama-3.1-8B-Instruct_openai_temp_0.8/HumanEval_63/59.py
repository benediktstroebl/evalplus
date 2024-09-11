```python
def fibfib(n: int) -> int:
    """
    Calculate the n-th element of the FibFib number sequence.

    The FibFib number sequence is a sequence similar to the Fibonacci sequence that's defined as follows:
    fibfib(0) == 0
    fibfib(1) == 0
    fibfib(2) == 1
    fibfib(n) == fibfib(n-1) + fibfib(n-2) + fibfib(n-3).

    Args:
        n (int): The index of the element in the sequence.

    Returns:
        int: The n-th element of the FibFib number sequence.
    """
    if n <= 1:
        return 0
    elif n == 2:
        return 1
    else:
        # Create a dictionary to store the already calculated values
        memo = {0: 0, 1: 0, 2: 1}
        
        # Calculate the remaining elements
        for i in range(3, n + 1):
            # Calculate the value using the formula and store it in the memo dictionary
            memo[i] = memo[i - 1] + memo[i - 2] + memo[i - 3]
        
        # Return the calculated n-th element
        return memo[n]

# Test cases
print(fibfib(1))  # Output: 0
print(fibfib(5))  # Output: 4
print(fibfib(8))  # Output: 24
```

This script uses a dictionary called `memo` to store the calculated values of the FibFib sequence. It avoids redundant calculations by using these stored values, making it more efficient for larger values of `n`.