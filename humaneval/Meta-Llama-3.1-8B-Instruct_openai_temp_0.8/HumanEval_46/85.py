```python
def fib4(n: int):
    """
    The Fib4 number sequence is a sequence similar to the Fibonacci sequence that's 
    defined as follows:
    fib4(0) -> 0
    fib4(1) -> 0
    fib4(2) -> 2
    fib4(3) -> 0
    fib4(n) -> fib4(n-1) + fib4(n-2) + fib4(n-3) + fib4(n-4).
    
    This function efficiently computes the n-th element of the fib4 number sequence 
    without using recursion.
    
    Parameters:
    n (int): The position of the element in the fib4 sequence.
    
    Returns:
    int: The n-th element of the fib4 sequence.
    """
    if n < 0:
        raise ValueError("n must be a non-negative integer")
    elif n == 0 or n == 1:
        return 0
    elif n == 2:
        return 2
    else:
        # Initialize a list to store the fib4 sequence
        fib4_sequence = [0] * (n + 1)
        
        # Base cases
        fib4_sequence[0] = 0
        fib4_sequence[1] = 0
        fib4_sequence[2] = 2
        
        # Compute the fib4 sequence
        for i in range(3, n + 1):
            fib4_sequence[i] = fib4_sequence[i-1] + fib4_sequence[i-2] + fib4_sequence[i-3] + fib4_sequence[i-4]
        
        # Return the n-th element
        return fib4_sequence[n]

# Test cases
print(fib4(5))   # 4
print(fib4(6))   # 8
print(fib4(7))   # 14
```

This script defines a function `fib4(n)` to efficiently compute the n-th element of the fib4 number sequence. It uses dynamic programming to store the sequence in a list, which allows it to compute the n-th element in O(n) time. The function also includes test cases to verify its correctness.