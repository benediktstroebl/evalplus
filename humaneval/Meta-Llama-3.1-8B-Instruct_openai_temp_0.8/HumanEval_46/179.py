**Fib4 Number Sequence Computation**
=====================================

Below is a Python script that efficiently computes the n-th element of the fib4 number sequence using dynamic programming.

```markdown
def fib4(n: int):
    """
    The Fib4 number sequence is a sequence similar to the Fibbonacci sequence that's defined as follows:
    fib4(0) -> 0
    fib4(1) -> 0
    fib4(2) -> 2
    fib4(3) -> 0
    fib4(n) -> fib4(n-1) + fib4(n-2) + fib4(n-3) + fib4(n-4).
    
    Args:
        n (int): The position of the Fib4 number to compute.
    
    Returns:
        int: The n-th element of the Fib4 number sequence.
    """
    
    # Base cases
    if n == 0 or n == 1:
        return 0
    
    # Initialize a list to store the computed Fib4 numbers
    fib4_nums = [0] * (n + 1)
    
    # Initialize the first four elements
    fib4_nums[0] = 0
    fib4_nums[1] = 0
    fib4_nums[2] = 2
    fib4_nums[3] = 0
    
    # Compute the remaining elements iteratively
    for i in range(4, n + 1):
        fib4_nums[i] = fib4_nums[i - 1] + fib4_nums[i - 2] + fib4_nums[i - 3] + fib4_nums[i - 4]
    
    # Return the n-th Fib4 number
    return fib4_nums[n]

# Test cases
print(fib4(5))   # Output: 4
print(fib4(6))   # Output: 8
print(fib4(7))   # Output: 14
```

In this script, we use dynamic programming to efficiently compute the n-th element of the fib4 number sequence. We store the computed Fib4 numbers in a list and use the previously computed values to calculate the next element. This approach reduces the time complexity to O(n) compared to the naive recursive approach.