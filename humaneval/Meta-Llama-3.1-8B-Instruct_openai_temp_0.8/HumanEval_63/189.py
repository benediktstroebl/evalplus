```python
def fibfib(n: int):
    """
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
        # Initialize a list to store the fibfib sequence
        fibfib_sequence = [0, 0, 1] + [0]*(n-2)
        
        # Compute the fibfib sequence
        for i in range(3, n+1):
            fibfib_sequence[i] = fibfib_sequence[i-1] + fibfib_sequence[i-2] + fibfib_sequence[i-3]
        
        # Return the n-th element
        return fibfib_sequence[n]

# Test cases
print(fibfib(1))  # Output: 0
print(fibfib(5))  # Output: 4
print(fibfib(8))  # Output: 24
```

This script defines the `fibfib` function which computes the n-th element of the FibFib number sequence using a technique called memoization (storing the result of expensive function calls and reusing them when the same inputs occur again). The time complexity of this function is O(n) and the space complexity is also O(n).