```python
def fib4(n: int):
    """
    The Fib4 number sequence is a sequence similar to the Fibbonacci sequence 
    that's defined as follows:
    fib4(0) -> 0
    fib4(1) -> 0
    fib4(2) -> 2
    fib4(3) -> 0
    fib4(n) -> fib4(n-1) + fib4(n-2) + fib4(n-3) + fib4(n-4).
    
    Args:
        n (int): The position of the element in the sequence.
    
    Returns:
        int: The nth element of the fib4 number sequence.
    """
    if n <= 1:
        return 0
    elif n == 2:
        return 2
    elif n == 3:
        return 0
    
    # Initialize an array to store the fib4 numbers
    fib4_numbers = [0, 0, 2, 0] + [0]*(n-3)
    
    # Compute the fib4 numbers iteratively
    for i in range(4, n+1):
        fib4_numbers[i-1] = fib4_numbers[i-2] + fib4_numbers[i-3] + fib4_numbers[i-4]
    
    return fib4_numbers[n-1]

# Test the function
print(fib4(5))  # Output: 4
print(fib4(6))  # Output: 8
print(fib4(7))  # Output: 14
```

This script defines a function `fib4(n)` that efficiently computes the nth element of the fib4 number sequence using iteration. It first checks for the base cases, then initializes an array to store the fib4 numbers. The function then iterates from the 4th position to compute the fib4 numbers iteratively. Finally, it returns the nth element of the fib4 number sequence.