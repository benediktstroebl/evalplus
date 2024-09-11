### Fib4 Number Sequence Computation
#### Efficient Computation of the n-th Element

```python
def fib4(n: int) -> int:
    """
    Compute the n-th element of the Fib4 number sequence.

    The Fib4 number sequence is defined as follows:
    fib4(0) -> 0
    fib4(1) -> 0
    fib4(2) -> 2
    fib4(3) -> 0
    fib4(n) -> fib4(n-1) + fib4(n-2) + fib4(n-3) + fib4(n-4).

    Args:
        n (int): The index of the element to compute.

    Returns:
        int: The n-th element of the Fib4 number sequence.

    Example:
        >>> fib4(5)
        4
        >>> fib4(6)
        8
        >>> fib4(7)
        14
    """

    # Base cases for memoization
    if n == 0 or n == 1:
        return 0
    elif n == 2:
        return 2
    elif n < 0:
        raise ValueError("Negative indices are not supported")

    # Initialize the base of the sequence
    a, b, c, d = 0, 0, 2, 0

    # Compute the sequence up to the n-th element
    for _ in range(3, n + 1):
        # Update the sequence using the previous four elements
        a, b, c, d = b, c, d, a + b + c + d

    return d

# Test cases
if __name__ == "__main__":
    print(fib4(5))  # Output: 4
    print(fib4(6))  # Output: 8
    print(fib4(7))  # Output: 14
```

This script uses an iterative approach with memoization to efficiently compute the n-th element of the Fib4 number sequence. The base cases are handled directly, and the remaining elements are computed using a loop with four variables to store the previous four elements in the sequence. This approach reduces the time complexity to O(n), making it efficient for large values of n.