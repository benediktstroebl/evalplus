```python
def fibfib(n: int) -> int:
    """
    The FibFib number sequence is a sequence similar to the Fibonacci sequence 
    that's defined as follows:
    fibfib(0) == 0
    fibfib(1) == 0
    fibfib(2) == 1
    fibfib(n) == fibfib(n-1) + fibfib(n-2) + fibfib(n-3).

    This function efficiently computes the n-th element of the fibfib number sequence.

    Args:
        n (int): The index of the element in the fibfib sequence.

    Returns:
        int: The n-th element of the fibfib sequence.
    """
    if n < 0:
        raise ValueError("Input should be a non-negative integer.")
    
    # Base cases
    if n == 0:
        return 0
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    
    # Initialize a list to store the fibfib numbers
    fibfib_sequence = [0, 0, 1]
    
    # Compute the fibfib numbers up to the n-th element
    for i in range(3, n + 1):
        # Compute the i-th element as the sum of the three preceding elements
        fibfib_sequence.append(fibfib_sequence[i - 1] + fibfib_sequence[i - 2] + fibfib_sequence[i - 3])
    
    # Return the n-th element
    return fibfib_sequence[n]


# Test cases
print(fibfib(1))  # Output: 0
print(fibfib(5))  # Output: 4
print(fibfib(8))  # Output: 24
```

This script uses a bottom-up dynamic programming approach to efficiently compute the n-th element of the fibfib number sequence. It initializes a list to store the computed fibfib numbers and iteratively fills up the list until it reaches the n-th element. The time complexity of this approach is O(n), making it suitable for large inputs.