```python
def fib4(n: int):
    """
    The Fib4 number sequence is a sequence similar to the Fibbonacci sequence that's defined as follows:
    fib4(0) -> 0
    fib4(1) -> 0
    fib4(2) -> 2
    fib4(3) -> 0
    fib4(n) -> fib4(n-1) + fib4(n-2) + fib4(n-3) + fib4(n-4).
    
    This function efficiently computes the n-th element of the fib4 number sequence using dynamic programming.
    
    Args:
    n (int): The position of the number in the sequence.
    
    Returns:
    int: The n-th number in the fib4 sequence.
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
    
    # Initialize the array to store the fib4 numbers
    fib4_numbers = [0, 0, 2, 0]
    
    # Compute the fib4 numbers from n=4 to n
    for i in range(4, n + 1):
        # fib4(i) = fib4(i-1) + fib4(i-2) + fib4(i-3) + fib4(i-4)
        fib4_numbers.append(fib4_numbers[i-1] + fib4_numbers[i-2] + fib4_numbers[i-3] + fib4_numbers[i-4])
    
    # Return the n-th fib4 number
    return fib4_numbers[n]

# Test the function
print(fib4(5))  # Output: 4
print(fib4(6))  # Output: 8
print(fib4(7))  # Output: 14
```

This script first checks for the base cases, then initializes an array to store the fib4 numbers. It then computes the fib4 numbers from n=4 to n using a loop, and finally returns the n-th fib4 number. The function uses dynamic programming to efficiently compute the fib4 numbers.