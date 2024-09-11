```python
def fibfib(n: int) -> int:
    """
    The FibFib number sequence is a sequence similar to the Fibonacci sequence that's defined as follows:
    fibfib(0) == 0
    fibfib(1) == 0
    fibfib(2) == 1
    fibfib(n) == fibfib(n-1) + fibfib(n-2) + fibfib(n-3).

    Args:
        n (int): The position of the number in the FibFib sequence.

    Returns:
        int: The nth number in the FibFib sequence.

    Raises:
        ValueError: If n is less than 0.
    """
    if n < 0:
        raise ValueError("n must be a non-negative integer")

    # Base cases
    if n == 0:
        return 0
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    # Compute Fibonacci numbers on the fly to save memory
    elif n == 3:
        return 1
    else:
        a, b, c = 0, 0, 1
        for _ in range(3, n + 1):
            a, b, c = b, c, a + b + c
        return c

# Test cases
print(fibfib(1))  # 0
print(fibfib(5))  # 4
print(fibfib(8))  # 24
```

This script uses an iterative approach to compute the nth number in the FibFib sequence, which has a time complexity of O(n) and a space complexity of O(1) as it only uses a constant amount of space to store the last three numbers in the sequence. The function raises a ValueError if n is less than 0.