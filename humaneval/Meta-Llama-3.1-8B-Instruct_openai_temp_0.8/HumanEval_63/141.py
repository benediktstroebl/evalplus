```python
# Define a function to calculate the nth element of the FibFib number sequence
def fibfib(n: int) -> int:
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
    int: The nth element of the FibFib number sequence.
    """
    if n <= 0:
        return 0
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        a, b, c = 0, 0, 1
        for _ in range(3, n + 1):
            a, b, c = b, c, a + b + c
        return c

# Test the function
print(fibfib(1))  # Expected output: 0
print(fibfib(5))  # Expected output: 4
print(fibfib(8))  # Expected output: 24
```

This script defines a function `fibfib(n)` that calculates the nth element of the FibFib number sequence. It uses dynamic programming to memoize the previous three elements of the sequence to avoid redundant calculations, which leads to an efficient computation. The function is then tested with the provided example use cases.