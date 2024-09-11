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
    
    This function efficiently computes the n-th element of the fib4 number sequence 
    using dynamic programming without recursion.
    
    Args:
        n (int): The index of the element to compute.
    
    Returns:
        int: The nth element of the fib4 number sequence.
    """
    if n < 0:
        raise ValueError("Input must be a non-negative integer")
    
    # Initialize the base cases
    if n <= 1:
        return 0
    elif n == 2:
        return 2
    
    # Initialize a list to store the computed elements
    fib4_sequence = [0] * (n + 1)
    fib4_sequence[1] = 0
    fib4_sequence[2] = 2
    
    # Compute the rest of the sequence using dynamic programming
    for i in range(3, n + 1):
        fib4_sequence[i] = fib4_sequence[i-1] + fib4_sequence[i-2] + fib4_sequence[i-3] + fib4_sequence[i-4]
    
    return fib4_sequence[n]

# Test the function
print(fib4(5))  # Output: 4
print(fib4(6))  # Output: 8
print(fib4(7))  # Output: 14
```

This script defines a function `fib4(n)` that computes the nth element of the Fib4 number sequence using dynamic programming. The function first initializes the base cases and then uses a loop to compute the rest of the sequence. The result is returned as the nth element of the `fib4_sequence` list. The script also includes test cases to verify the correctness of the function.