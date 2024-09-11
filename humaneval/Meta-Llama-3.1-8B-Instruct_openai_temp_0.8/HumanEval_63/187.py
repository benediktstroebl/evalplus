```python
def fibfib(n: int) -> int:
    """
    The FibFib number sequence is a sequence similar to the Fibonacci sequence that's defined as follows:
    fibfib(0) == 0
    fibfib(1) == 0
    fibfib(2) == 1
    fibfib(n) == fibfib(n-1) + fibfib(n-2) + fibfib(n-3).
    
    Args:
    n (int): The index of the FibFib number to compute.

    Returns:
    int: The n-th element of the FibFib number sequence.
    """
    if n == 0 or n == 1:
        return 0
    elif n == 2:
        return 1

    # Initialize a list to store the computed values, since fibfib(n) depends on fibfib(n-1), fibfib(n-2), and fibfib(n-3)
    fibfib_values = [0, 0, 1]

    # Compute and store the values from fibfib(3) to fibfib(n)
    for i in range(3, n + 1):
        # Compute fibfib(i) as the sum of fibfib(i-1), fibfib(i-2), and fibfib(i-3)
        fibfib_values.append(fibfib_values[i - 1] + fibfib_values[i - 2] + fibfib_values[i - 3])

    # Return the computed value of fibfib(n)
    return fibfib_values[n]


# Test the function with the provided test cases
print(fibfib(1))  # Expected output: 0
print(fibfib(5))  # Expected output: 4
print(fibfib(8))  # Expected output: 24
```

This script uses a simple iterative approach to compute the n-th element of the FibFib number sequence. It initializes a list to store the computed values and uses a loop to compute and store the values from fibfib(3) to fibfib(n). The computed value of fibfib(n) is then returned.