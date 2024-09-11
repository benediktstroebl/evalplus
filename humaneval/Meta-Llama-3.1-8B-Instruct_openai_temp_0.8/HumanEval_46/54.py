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
    """
    if n <= 3:
        return [0, 0, 2, 0][n]
    
    fib4_sequence = [0, 0, 2, 0]
    for i in range(4, n + 1):
        fib4_sequence.append(fib4_sequence[i-1] + fib4_sequence[i-2] + fib4_sequence[i-3] + fib4_sequence[i-4])
        
    return fib4_sequence[n]

# Test the function
print(fib4(5))   # Output: 4
print(fib4(6))   # Output: 8
print(fib4(7))   # Output: 14
```

This script uses an iterative approach to compute the n-th element of the fib4 sequence. It uses an array to store the previously computed values, and then it uses these values to compute the next value in the sequence. This approach makes it more efficient than using recursion.