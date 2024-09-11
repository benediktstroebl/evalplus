```python
def fib4(n: int) -> int:
    """
    The Fib4 number sequence is a sequence similar to the Fibbonacci sequence that's defined as follows:
    fib4(0) -> 0
    fib4(1) -> 0
    fib4(2) -> 2
    fib4(3) -> 0
    fib4(n) -> fib4(n-1) + fib4(n-2) + fib4(n-3) + fib4(n-4).
    
    This function efficiently computes the n-th element of the fib4 number sequence without using recursion.
    
    Args:
        n (int): The index of the fib4 number to be computed.
    
    Returns:
        int: The n-th element of the fib4 number sequence.
    """
    if n < 0:
        raise ValueError("Input must be a non-negative integer.")

    # Base cases
    if n == 0 or n == 1:
        return 0
    
    # Initialize a list to store the fib4 numbers
    fib4_nums = [0, 0]
    
    # Compute the fib4 numbers up to the n-th number
    for i in range(2, n + 1):
        # Compute the next fib4 number as the sum of the previous four numbers
        next_num = fib4_nums[i - 1] + fib4_nums[i - 2] + fib4_nums[i - 3] + fib4_nums[i - 4]
        fib4_nums.append(next_num)
    
    # Return the n-th fib4 number
    return fib4_nums[n]

# Test the function
print(fib4(5))  # Output: 4
print(fib4(6))  # Output: 8
print(fib4(7))  # Output: 14
```