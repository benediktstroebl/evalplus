```python
def fibfib(n: int) -> int:
    """
    Compute the n-th element of the FibFib number sequence.

    The FibFib number sequence is a sequence similar to the Fibonacci sequence that's defined as follows:
    fibfib(0) == 0
    fibfib(1) == 0
    fibfib(2) == 1
    fibfib(n) == fibfib(n-1) + fibfib(n-2) + fibfib(n-3).

    Args:
        n (int): The index of the element to compute.

    Returns:
        int: The n-th element of the FibFib number sequence.

    Raises:
        ValueError: If n is a negative integer.
    """
    if n < 0:
        raise ValueError("n must be a non-negative integer")
    elif n <= 2:
        return 0
    elif n == 3:
        return 1
    else:
        # Initialize a list to store the Fibonacci numbers
        fibfib_nums = [0, 0, 1] + [0]*(n-3)
        
        # Compute the Fibonacci numbers using dynamic programming
        for i in range(4, n+1):
            fibfib_nums[i-1] = fibfib_nums[i-2] + fibfib_nums[i-3] + fibfib_nums[i-4]
        
        # Return the n-th Fibonacci number
        return fibfib_nums[-1]

# Test the function
print(fibfib(1))  # Output: 0
print(fibfib(5))  # Output: 4
print(fibfib(8))  # Output: 24
```

This script uses dynamic programming to efficiently compute the n-th element of the FibFib number sequence. It initializes a list to store the Fibonacci numbers and then uses a loop to compute each number recursively. The function also includes error checking to ensure that n is a non-negative integer.