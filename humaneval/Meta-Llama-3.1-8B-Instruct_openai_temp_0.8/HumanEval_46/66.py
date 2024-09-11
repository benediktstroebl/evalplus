### Fib4 Number Sequence
#### A Python Implementation

```python
def fib4(n: int) -> int:
    """
    Compute the n-th element of the Fib4 number sequence.

    The Fib4 number sequence is a sequence similar to the Fibonacci sequence, 
    defined as follows:
    fib4(0) -> 0
    fib4(1) -> 0
    fib4(2) -> 2
    fib4(3) -> 0
    fib4(n) -> fib4(n-1) + fib4(n-2) + fib4(n-3) + fib4(n-4).

    Parameters:
    n (int): The index of the element to compute.

    Returns:
    int: The n-th element of the Fib4 number sequence.
    """
    if n < 4:
        # Base cases
        return 0 if n in (0, 1) else 2 if n == 2 else 0

    # Initialize the first four elements
    a, b, c, d = 0, 0, 2, 0

    # Compute the remaining elements
    for _ in range(4, n + 1):
        # Calculate the next element as the sum of the previous four
        a, b, c, d = b, c, d, a + b + c + d

    # Return the n-th element
    return d

# Test cases
print(fib4(5))  # 4
print(fib4(6))  # 8
print(fib4(7))  # 14
```

This script defines a function `fib4` that computes the n-th element of the Fib4 number sequence. It uses an iterative approach with a constant time complexity of O(n), making it efficient for large values of n. The base cases and the recurrence relation are handled explicitly to ensure correctness.