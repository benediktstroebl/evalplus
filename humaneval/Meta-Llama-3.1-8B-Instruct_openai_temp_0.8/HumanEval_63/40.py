```python
def fibfib(n: int):
    """
    The FibFib number sequence is a sequence similar to the Fibonacci sequence 
    that's defined as follows:
    fibfib(0) == 0
    fibfib(1) == 0
    fibfib(2) == 1
    fibfib(n) == fibfib(n-1) + fibfib(n-2) + fibfib(n-3).
    
    Args:
    n (int): The position of the number in the FibFib sequence.
    
    Returns:
    int: The nth element of the FibFib sequence.
    """
    if n <= 1:
        return 0
    elif n == 2:
        return 1
    elif n == 3:
        return 1
    else:
        a, b, c = 0, 0, 1
        for _ in range(3, n + 1):
            a, b, c = b, c, a + b + c
        return c

# Test cases
print(fibfib(1))  # Expected output: 0
print(fibfib(5))  # Expected output: 4
print(fibfib(8))  # Expected output: 24
```

This code first checks for the base cases (n <= 1, n == 2, or n == 3) and returns the corresponding value. For larger values of n, it uses the formula `a, b, c = b, c, a + b + c` to compute the nth element in constant time per iteration.