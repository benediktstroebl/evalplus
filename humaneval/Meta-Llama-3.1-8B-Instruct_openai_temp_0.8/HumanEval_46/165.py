```python
def fib4(n: int):
    """
    The Fib4 number sequence is a sequence similar to the Fibonacci sequence that's defined as follows:
    fib4(0) -> 0
    fib4(1) -> 0
    fib4(2) -> 2
    fib4(3) -> 0
    fib4(n) -> fib4(n-1) + fib4(n-2) + fib4(n-3) + fib4(n-4).
    
    This function efficiently computes the n-th element of the fib4 number sequence using dynamic programming.
    
    Args:
    n (int): The index of the element to compute in the fib4 sequence.
    
    Returns:
    int: The n-th element of the fib4 sequence.
    """
    if n <= 3:
        # Base cases for the sequence
        return [0, 0, 2, 0][n]
    
    # Initialize the list to store the fib4 numbers, with the first four numbers filled in
    fib4_nums = [0, 0, 2, 0]
    
    # Compute the fib4 numbers iteratively
    for i in range(4, n + 1):
        fib4_nums.append(fib4_nums[i - 1] + fib4_nums[i - 2] + fib4_nums[i - 3] + fib4_nums[i - 4])
    
    # Return the n-th element of the fib4 sequence
    return fib4_nums[n]

# Test the function
print(fib4(5))  # Expected output: 4
print(fib4(6))  # Expected output: 8
print(fib4(7))  # Expected output: 14
```

This script uses dynamic programming to compute the n-th element of the fib4 number sequence in O(n) time complexity. It initializes a list to store the fib4 numbers and then iteratively computes the numbers using the recurrence relation. The base cases are handled separately to avoid recursion. The test cases are included at the end to verify the correctness of the function.