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
        n (int): The position of the number in the sequence.
    
    Returns:
        int: The n-th element of the fib4 number sequence.
    """
    # Handle edge cases
    if n == 0:
        return 0
    elif n == 1:
        return 0
    elif n == 2:
        return 2
    elif n == 3:
        return 0
    
    # Initialize a list to store the fib4 numbers
    fib4_nums = [0]*5
    
    # Compute the first 4 fib4 numbers
    fib4_nums[0] = 0
    fib4_nums[1] = 0
    fib4_nums[2] = 2
    fib4_nums[3] = 0
    
    # Compute the remaining fib4 numbers
    for i in range(4, n+1):
        fib4_nums[i] = fib4_nums[i-1] + fib4_nums[i-2] + fib4_nums[i-3] + fib4_nums[i-4]
    
    # Return the n-th element
    return fib4_nums[n]

# Test the function
print(fib4(5))  # 4
print(fib4(6))  # 8
print(fib4(7))  # 14
```

This script uses a bottom-up dynamic programming approach to efficiently compute the n-th element of the fib4 number sequence. It initializes a list to store the fib4 numbers, computes the first 4 fib4 numbers, and then uses a for loop to compute the remaining fib4 numbers. Finally, it returns the n-th element of the list.