```python
def fib4(n: int) -> int:
    """
    The Fib4 number sequence is a sequence similar to the Fibonacci sequence that's defined as follows:
    fib4(0) -> 0
    fib4(1) -> 0
    fib4(2) -> 2
    fib4(3) -> 0
    fib4(n) -> fib4(n-1) + fib4(n-2) + fib4(n-3) + fib4(n-4).

    Args:
        n: The index of the sequence to compute.

    Returns:
        The nth element of the Fib4 number sequence.
    """
    if n < 0:
        raise ValueError("n must be a non-negative integer")

    # Base cases
    if n == 0 or n == 1:
        return 0
    elif n == 2:
        return 2
    elif n == 3:
        return 0

    # Initialize the first four elements
    a, b, c, d = 0, 0, 2, 0

    # Compute the nth element
    for _ in range(4, n + 1):
        # Update the last four elements
        a, b, c, d = b, c, d, a + b + c + d

    return d

# Test cases
print(fib4(5))  # 4
print(fib4(6))  # 8
print(fib4(7))  # 14
```

This script defines a function `fib4` that computes the nth element of the Fib4 number sequence using a loop, avoiding recursion. It handles edge cases and returns the correct results. The test cases are included to demonstrate the function's correctness.