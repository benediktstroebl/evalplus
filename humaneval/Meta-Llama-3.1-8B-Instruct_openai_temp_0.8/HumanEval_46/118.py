```python
def fib4(n: int):
    """
    The Fib4 number sequence is a sequence similar to the Fibbonacci sequence that's defined as follows:
    fib4(0) -> 0
    fib4(1) -> 0
    fib4(2) -> 2
    fib4(3) -> 0
    fib4(n) -> fib4(n-1) + fib4(n-2) + fib4(n-3) + fib4(n-4).
    
    This function efficiently computes the n-th element of the fib4 number sequence without using recursion.
    """
    if n < 0:
        raise ValueError("Input must be a non-negative integer.")
    
    # Initialize a list to store the fib4 numbers
    fib4_nums = [0, 0, 2, 0]
    
    # If n is within the bounds of the base cases, return the corresponding number
    if n <= 3:
        return fib4_nums[n]
    
    # Compute the fib4 numbers up to the nth number
    for i in range(4, n + 1):
        # The ith fib4 number is the sum of the (i-1)th, (i-2)th, (i-3)th, and (i-4)th numbers
        fib4_nums.append(fib4_nums[i-1] + fib4_nums[i-2] + fib4_nums[i-3] + fib4_nums[i-4])
    
    # Return the nth fib4 number
    return fib4_nums[n]

# Test the function
print(fib4(5))  # Output: 4
print(fib4(6))  # Output: 8
print(fib4(7))  # Output: 14
```

This script defines the `fib4` function, which efficiently computes the n-th element of the fib4 number sequence without using recursion. It uses a list to store the fib4 numbers up to the nth number, which allows it to compute the fib4 numbers in linear time. The function also handles invalid input by raising a `ValueError` if the input is a negative integer.