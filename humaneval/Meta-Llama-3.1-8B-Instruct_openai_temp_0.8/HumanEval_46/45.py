```python
def fib4(n: int) -> int:
    """
    The Fib4 number sequence is a sequence similar to the Fibonacci sequence 
    that's defined as follows:
    fib4(0) -> 0
    fib4(1) -> 0
    fib4(2) -> 2
    fib4(3) -> 0
    fib4(n) -> fib4(n-1) + fib4(n-2) + fib4(n-3) + fib4(n-4).
    
    This function efficiently computes the n-th element of the fib4 number sequence 
    using dynamic programming.
    
    Parameters:
    n (int): The index of the element in the fib4 sequence.
    
    Returns:
    int: The n-th element of the fib4 sequence.
    """
    
    # Base cases
    if n == 0:
        return 0
    elif n == 1:
        return 0
    elif n == 2:
        return 2
    elif n == 3:
        return 0
    
    # Initialize an array to store fib4 numbers
    fib4_n = [0] * (n + 1)
    fib4_n[0] = 0
    fib4_n[1] = 0
    fib4_n[2] = 2
    fib4_n[3] = 0
    
    # Compute fib4 numbers iteratively
    for i in range(4, n + 1):
        fib4_n[i] = fib4_n[i - 1] + fib4_n[i - 2] + fib4_n[i - 3] + fib4_n[i - 4]
    
    # Return the n-th element
    return fib4_n[n]

# Test the function
print(fib4(5))     # Output: 4
print(fib4(6))     # Output: 8
print(fib4(7))     # Output: 14
```

This script uses dynamic programming to compute the n-th element of the fib4 sequence. It first initializes an array to store the fib4 numbers, then iteratively computes each element from the 4th to the n-th. This approach has a time complexity of O(n) and a space complexity of O(n), making it efficient for large values of n.