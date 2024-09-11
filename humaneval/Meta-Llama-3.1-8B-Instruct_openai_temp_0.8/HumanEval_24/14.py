```python
def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    
    Args:
        n (int): The input number.
    
    Returns:
        int: The largest divisor of n smaller than n.
    
    Example:
        >>> largest_divisor(15)
        5
    """
    for i in range(n - 1, 0, -1):
        if n % i == 0:
            return i
    return 1

# Test the function
print(largest_divisor(15))  # Output: 5
print(largest_divisor(20))  # Output: 10
```

This script defines a function `largest_divisor(n)` that iterates over all numbers from `n-1` down to 1, checking if `n` is divisible by the current number. As soon as it finds such a number, it returns it. If it doesn't find any divisor (which should not happen for any positive integer), it returns 1. The test cases at the end check the function's correctness.