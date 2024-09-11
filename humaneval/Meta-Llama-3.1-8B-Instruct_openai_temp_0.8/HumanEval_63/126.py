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
    n (int): The position of the element in the sequence.

    Returns:
    int: The n-th element of the fibfib number sequence.
    """
    if n <= 0:
        return 0
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        # Initialize a list to store the last three numbers in the sequence
        a, b, c = 0, 0, 1
        for _ in range(3, n + 1):
            # Update the last three numbers in the sequence
            a, b, c = b, c, a + b + c
        return c

# Test the function
print(fibfib(1))  # Should print: 0
print(fibfib(5))  # Should print: 4
print(fibfib(8))  # Should print: 24
```

This script defines a function `fibfib(n)` that computes the n-th element of the FibFib number sequence. The function uses a loop to store the last three numbers in the sequence, and then updates them to calculate the next number in the sequence. This approach is more efficient than recalculating the sequence from scratch for each call.