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
    
    This function efficiently computes the n-th element of the fib4 number sequence.
    
    Args:
    n (int): The index of the element in the sequence.
    
    Returns:
    int: The n-th element of the fib4 number sequence.
    """
    if n <= 1:
        return 0
    elif n == 2:
        return 2
    elif n == 3:
        return 0
    else:
        a, b, c, d = 0, 0, 2, 0
        for _ in range(4, n + 1):
            a, b, c, d = b, c, d, a + b + c + d
        return d

# Test cases
print(fib4(5))  # Output: 4
print(fib4(6))  # Output: 8
print(fib4(7))  # Output: 14
```

This script defines the `fib4` function, which uses a loop to compute the n-th element of the fib4 number sequence. It initializes four variables `a`, `b`, `c`, and `d` with the first four elements of the sequence (0, 0, 2, 0) and then iteratively updates these variables according to the recursive formula. The final value of `d` is the n-th element of the sequence.