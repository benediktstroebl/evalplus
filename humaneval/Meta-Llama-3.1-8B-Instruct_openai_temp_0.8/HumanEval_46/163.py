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
    
    Parameters:
    n (int): The index of the Fib4 number to compute.
    
    Returns:
    int: The n-th element of the Fib4 number sequence.
    """
    if n < 0:
        raise ValueError("n must be a non-negative integer")
    
    # Base cases for the Fibonacci sequence
    if n == 0 or n == 1:
        return 0
    elif n == 2:
        return 2
    elif n == 3:
        return 0
    
    # Initialize an array to store the Fibonacci numbers
    fib4_sequence = [0] * (n + 1)
    fib4_sequence[0] = 0
    fib4_sequence[1] = 0
    fib4_sequence[2] = 2
    fib4_sequence[3] = 0
    
    # Compute the Fibonacci numbers iteratively
    for i in range(4, n + 1):
        fib4_sequence[i] = fib4_sequence[i-1] + fib4_sequence[i-2] + fib4_sequence[i-3] + fib4_sequence[i-4]
    
    return fib4_sequence[n]

# Test cases
print(fib4(5))   # 4
print(fib4(6))   # 8
print(fib4(7))   # 14
```

This script uses a dynamic programming approach to efficiently compute the n-th element of the Fib4 number sequence. It initializes an array to store the Fibonacci numbers and computes them iteratively, avoiding recursion. The base cases for the Fibonacci sequence are handled separately. The test cases at the end of the script verify that the function works correctly.