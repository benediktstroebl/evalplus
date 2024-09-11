```python
def fibfib(n: int) -> int:
    """
    The FibFib number sequence is a sequence similar to the Fibbonacci sequence that's defined as follows:
    fibfib(0) == 0
    fibfib(1) == 0
    fibfib(2) == 1
    fibfib(n) == fibfib(n-1) + fibfib(n-2) + fibfib(n-3).

    Args:
        n (int): The position of the number in the sequence.

    Returns:
        int: The n-th element of the FibFib number sequence.
    """
    if n < 0:
        raise ValueError("n must be a non-negative integer")
    elif n <= 1:
        return 0
    elif n == 2:
        return 1
    elif n > 2:
        # Store the last 3 values to avoid redundant calculations
        a, b, c = 0, 0, 1
        for _ in range(3, n + 1):
            a, b, c = b, c, b + c + a
        return c

# Test cases
print(fibfib(1))  # 0
print(fibfib(5))  # 4
print(fibfib(8))  # 24
```

This script defines a function `fibfib(n)` that calculates the n-th element of the FibFib number sequence using memoization. The function starts by checking if `n` is less than 0, in which case it raises a ValueError. If `n` is 0 or 1, it returns 0. If `n` is 2, it returns 1. For `n` values greater than 2, it uses a loop to calculate the n-th element and stores the last 3 values to avoid redundant calculations. The test cases at the end verify the function's correctness.