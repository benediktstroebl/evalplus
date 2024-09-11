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
        n (int): The position in the sequence to compute.

    Returns:
        int: The nth element of the Fib4 number sequence.
    """
    if n < 0:
        raise ValueError("n must be a non-negative integer")

    # Create lists to store the last four terms
    a, b, c, d = 0, 0, 2, 0

    # Iterate from 4 to n (inclusive)
    for _ in range(4, n + 1):
        # Update the last four terms
        a, b, c, d = b, c, d, a + b + c + d

    # Return the nth term
    return d


# Test the function
print(fib4(5))   # Output: 4
print(fib4(6))   # Output: 8
print(fib4(7))   # Output: 14
```

This script uses an iterative approach to compute the nth element of the Fib4 number sequence. It uses lists to store the last four terms of the sequence and updates them in each iteration. Finally, it returns the nth term. The time complexity of this script is O(n), which is more efficient than a recursive approach.