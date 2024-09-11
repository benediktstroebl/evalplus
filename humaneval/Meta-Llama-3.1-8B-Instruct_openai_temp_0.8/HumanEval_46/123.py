```python
def fib4(n: int) -> int:
    """
    The Fib4 number sequence is a sequence similar to the Fibbonacci sequence that's defined as follows:
    fib4(0) -> 0
    fib4(1) -> 0
    fib4(2) -> 2
    fib4(3) -> 0
    fib4(n) -> fib4(n-1) + fib4(n-2) + fib4(n-3) + fib4(n-4).

    Args:
        n (int): The index of the element in the fib4 number sequence.

    Returns:
        int: The n-th element of the fib4 number sequence.

    >>> fib4(5)
    4
    >>> fib4(6)
    8
    >>> fib4(7)
    14
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
    
    # Initialize the first four elements of the fib4 sequence
    a, b, c, d = 0, 0, 2, 0
    
    # Compute the n-th element
    for _ in range(4, n + 1):
        a, b, c, d = b, c, d, a + b + c + d
    
    return d

# Test cases
print(fib4(5))  # Output: 4
print(fib4(6))  # Output: 8
print(fib4(7))  # Output: 14
```

This Python script defines a function `fib4(n)` that computes the n-th element of the fib4 number sequence efficiently without using recursion. The function uses an iterative approach with a loop to compute the elements of the sequence. The base cases are handled separately, and the function returns the n-th element of the sequence. The script includes test cases to verify the correctness of the function.