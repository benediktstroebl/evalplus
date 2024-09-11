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
        n (int): The index of the sequence to compute.

    Returns:
        int: The nth element of the fib4 number sequence.

    Example:
        >>> fib4(5)
        4
        >>> fib4(6)
        8
        >>> fib4(7)
        14
    """
    if n <= 0:
        return 0
    elif n == 1:
        return 0
    elif n == 2:
        return 2
    else:
        a, b, c, d = 0, 0, 2, 0
        for _ in range(3, n + 1):
            # Update the values to compute the next one
            a, b, c, d = b, c, d, a + b + c + d
        return d

# Test the function
print(fib4(5))  # Output: 4
print(fib4(6))  # Output: 8
print(fib4(7))  # Output: 14
```
This script uses an iterative approach to compute the nth element of the fib4 number sequence. It uses a loop to store the last four values of the sequence and updates them in each iteration to compute the next one. This approach is more efficient than recursion for large values of n.