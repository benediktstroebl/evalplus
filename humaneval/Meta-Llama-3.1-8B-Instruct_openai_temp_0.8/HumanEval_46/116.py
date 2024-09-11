```python
def fib4(n: int):
    """
    Compute the n-th element of the fib4 number sequence.

    The fib4 number sequence is defined as follows:
    fib4(0) -> 0
    fib4(1) -> 0
    fib4(2) -> 2
    fib4(3) -> 0
    fib4(n) -> fib4(n-1) + fib4(n-2) + fib4(n-3) + fib4(n-4).

    Args:
        n (int): The index of the fib4 number to compute.

    Returns:
        int: The n-th element of the fib4 number sequence.
    """
    if n < 0:
        raise ValueError("n must be a non-negative integer")

    # Initialize the base cases of the fib4 sequence
    a, b, c, d = 0, 0, 2, 0

    # Compute each element of the fib4 sequence up to the nth element
    for _ in range(4, n + 1):
        a, b, c, d = b, c, d, (a + b + c + d)

    return d

# Test the function
print(fib4(5))  # Output: 4
print(fib4(6))  # Output: 8
print(fib4(7))  # Output: 14
```

This script uses an iterative approach to compute each element of the fib4 sequence up to the nth element, storing the last four elements in the variables `a`, `b`, `c`, and `d`. It then returns the nth element of the sequence. This approach has a time complexity of O(n) and a space complexity of O(1), making it efficient for large values of n.