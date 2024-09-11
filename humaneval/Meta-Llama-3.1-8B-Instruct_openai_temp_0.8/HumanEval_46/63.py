```python
def fib4(n: int) -> int:
    """
    Compute the n-th element of the fib4 number sequence.

    The fib4 number sequence is defined as:
    fib4(0) -> 0
    fib4(1) -> 0
    fib4(2) -> 2
    fib4(3) -> 0
    fib4(n) -> fib4(n-1) + fib4(n-2) + fib4(n-3) + fib4(n-4).

    Args:
    n: The index of the fib4 number sequence to compute.

    Returns:
    The n-th element of the fib4 number sequence.
    """
    fib4_sequence = [0, 0, 2, 0]  # Base cases: fib4(0), fib4(1), fib4(2), fib4(3)
    
    # Iterate from 4 to n (inclusive) to build the fib4 sequence
    for i in range(4, n + 1):
        # Compute the next element as the sum of the previous four elements
        fib4_sequence.append(fib4_sequence[i-1] + fib4_sequence[i-2] + fib4_sequence[i-3] + fib4_sequence[i-4])
    
    # Return the n-th element of the fib4 sequence
    return fib4_sequence[n]

# Test cases
print(fib4(5))  # Expected output: 4
print(fib4(6))  # Expected output: 8
print(fib4(7))  # Expected output: 14
```

This script uses an iterative approach to build the fib4 sequence up to the n-th element, which is then returned. The function starts with the base cases (0, 0, 2, 0) and iteratively computes each subsequent element as the sum of the previous four elements. This approach avoids the overhead of recursive function calls and is more efficient for large values of n.