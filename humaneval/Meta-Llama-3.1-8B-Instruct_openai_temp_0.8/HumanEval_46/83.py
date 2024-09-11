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
        n (int): The index of the Fib4 number to compute.
    
    Returns:
        int: The nth Fib4 number.
    """
    
    # Handle edge cases: fib4(0) -> 0 and fib4(1) -> 0
    if n <= 1:
        return 0
    
    # Handle fib4(2) -> 2
    if n == 2:
        return 2
    
    # Initialize a list to store the computed Fib4 numbers
    fib4_numbers = [0, 0, 2, 0]
    
    # Compute the nth Fib4 number iteratively
    for i in range(4, n + 1):
        # fib4(i) = fib4(i-1) + fib4(i-2) + fib4(i-3) + fib4(i-4)
        fib4_numbers.append(fib4_numbers[i-1] + fib4_numbers[i-2] + fib4_numbers[i-3] + fib4_numbers[i-4])
    
    # Return the computed nth Fib4 number
    return fib4_numbers[n]

# Test the function
print(fib4(5))  # Output: 4
print(fib4(6))  # Output: 8
print(fib4(7))  # Output: 14
```

In this script, we first handle the edge cases where `n` is 0, 1, or 2. Then we initialize a list `fib4_numbers` to store the computed Fib4 numbers. We iterate from `i = 4` to `n` and compute the `i-th` Fib4 number using the formula `fib4(i) = fib4(i-1) + fib4(i-2) + fib4(i-3) + fib4(i-4)`. Finally, we return the computed `n-th` Fib4 number.