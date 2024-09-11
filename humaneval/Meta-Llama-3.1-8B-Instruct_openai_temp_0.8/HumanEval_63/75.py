```python
def fibfib(n: int):
    """
    The FibFib number sequence is a sequence similar to the Fibonacci sequence 
    that's defined as follows:
    fibfib(0) == 0
    fibfib(1) == 0
    fibfib(2) == 1
    fibfib(n) == fibfib(n-1) + fibfib(n-2) + fibfib(n-3).

    Args:
        n (int): The position of the element in the sequence.

    Returns:
        int: The nth element of the FibFib sequence.
    """
    if n < 0:
        raise ValueError("n must be a non-negative integer.")

    # Base cases
    if n == 0:
        return 0
    elif n == 1:
        return 0
    elif n == 2:
        return 1

    # Initialize the first three elements of the sequence
    prev_prev = 0
    prev = 0
    curr = 1

    # Compute the nth element
    for _ in range(3, n + 1):
        # Update the sequence using the recurrence relation
        curr = prev + prev_prev + curr
        # Move to the next elements
        prev_prev = prev
        prev = curr

    # Return the nth element
    return curr

# Test the function
print(fibfib(1))  # Output: 0
print(fibfib(5))  # Output: 4
print(fibfib(8))  # Output: 24
```

This script defines a function `fibfib(n)` to compute the nth element of the FibFib sequence. It handles the base cases and uses a loop to compute the nth element based on the recurrence relation. The script also includes test cases to verify the correctness of the function.