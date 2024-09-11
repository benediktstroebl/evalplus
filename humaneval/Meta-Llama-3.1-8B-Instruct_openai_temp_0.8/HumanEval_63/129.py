```python
def fibfib(n: int) -> int:
    """
    The FibFib number sequence is a sequence similar to the Fibonacci sequence that's defined as follows:
    fibfib(0) == 0
    fibfib(1) == 0
    fibfib(2) == 1
    fibfib(n) == fibfib(n-1) + fibfib(n-2) + fibfib(n-3).
    
    Args:
        n (int): The index of the FibFib number to compute.
    
    Returns:
        int: The n-th element of the FibFib number sequence.
    """
    if n < 2:
        return 0
    elif n == 2:
        return 1
    elif n <= 3:
        return n
    else:
        a, b, c = 0, 0, 1
        for _ in range(3, n + 1):
            a, b, c = b, c, a + b + c
        return c

# Test the function
print(fibfib(1))  # Output: 0
print(fibfib(5))  # Output: 4
print(fibfib(8))  # Output: 24
```

This script defines a function `fibfib` that efficiently computes the n-th element of the FibFib number sequence. It uses a loop to calculate the elements iteratively, which reduces the time complexity from O(2^n) to O(n). The function also includes docstrings to describe its purpose, parameters, and return value. The test cases at the end verify that the function produces the correct results for the given inputs.