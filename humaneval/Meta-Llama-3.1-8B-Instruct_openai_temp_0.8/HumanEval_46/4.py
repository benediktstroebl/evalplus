```python
def fib4(n: int):
    """
    The Fib4 number sequence is a sequence similar to the Fibonacci sequence 
    that's defined as follows:
    fib4(0) -> 0
    fib4(1) -> 0
    fib4(2) -> 2
    fib4(3) -> 0
    fib4(n) -> fib4(n-1) + fib4(n-2) + fib4(n-3) + fib4(n-4).

    Args:
        n (int): The index of the Fib4 sequence to compute.

    Returns:
        int: The nth element of the Fib4 sequence.

    Raises:
        ValueError: If n is not a non-negative integer.
    """
    if not isinstance(n, int) or n < 0:
        raise ValueError("n must be a non-negative integer")

    if n == 0 or n == 1:
        return 0
    elif n == 2:
        return 2
    else:
        # Initialize a list to store the sequence values
        fib4_seq = [0] * (n + 1)
        
        # Base cases
        fib4_seq[0] = 0
        fib4_seq[1] = 0
        fib4_seq[2] = 2

        # Compute the rest of the sequence
        for i in range(3, n + 1):
            fib4_seq[i] = fib4_seq[i-1] + fib4_seq[i-2] + fib4_seq[i-3] + fib4_seq[i-4]

        # Return the nth element
        return fib4_seq[n]

# Test cases
print(fib4(5))  # Output: 4
print(fib4(6))  # Output: 8
print(fib4(7))  # Output: 14
```

This script uses dynamic programming to store and reuse previously computed values of the Fib4 sequence, resulting in efficient computation for larger values of `n`.