```python
def largest_divisor(n: int) -> int:
    """
    For a given number n, find the largest number that divides n evenly, smaller than n
    
    Args:
        n (int): The number to find the largest divisor for.
    
    Returns:
        int: The largest divisor of n.
    
    Examples:
        >>> largest_divisor(15)
        5
    """
    # Start from n-1 and go backwards until we find a divisor
    for i in range(n - 1, 0, -1):
        # Check if i is a divisor of n
        if n % i == 0:
            # If it is, return it as the largest divisor
            return i

# Test the function
print(largest_divisor(15))  # Output: 5
print(largest_divisor(10))  # Output: 5
print(largest_divisor(7))   # Output: 1
```

This script defines a function `largest_divisor` that finds the largest divisor of a given number `n`. It works by starting from `n-1` and going backwards, checking each number to see if it is a divisor of `n`. The first number it finds that is a divisor is returned as the largest divisor. The function includes a docstring that explains its purpose and usage.