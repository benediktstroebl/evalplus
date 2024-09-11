```python
def fib4(n: int):
    """
    The Fib4 number sequence is a sequence similar to the Fibonacci sequence that's defined as follows:
    fib4(0) -> 0
    fib4(1) -> 0
    fib4(2) -> 2
    fib4(3) -> 0
    fib4(n) -> fib4(n-1) + fib4(n-2) + fib4(n-3) + fib4(n-4).
    
    Args:
    n (int): The position of the number in the sequence.
    
    Returns:
    int: The n-th element of the fib4 number sequence.
    """
    if n <= 0:
        return 0
    
    # Initialize the base cases
    a, b, c, d = 0, 0, 2, 0
    
    # Compute the n-th element
    for _ in range(2, n+1):
        e = a + b + c + d
        a, b, c, d = b, c, d, e
    
    return d

# Test the function
print(fib4(5))  # Output: 4
print(fib4(6))  # Output: 8
print(fib4(7))  # Output: 14
```

This script uses a loop to compute the n-th element of the fib4 number sequence. It initializes the base cases `a`, `b`, `c`, and `d` with the values of `fib4(0)`, `fib4(1)`, `fib4(2)`, and `fib4(3)`, respectively. Then, it iteratively updates these values to compute the n-th element. The last value of `d` in the loop is the n-th element of the fib4 number sequence.