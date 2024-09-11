```python
def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    
    Args:
    n (int): A positive integer.
    
    Returns:
    int: The largest divisor of n.
    
    Examples:
    >>> largest_divisor(15)
    5
    """
    # Start from n-1 and check if it's a divisor of n
    for i in range(n-1, 0, -1):
        # If n is divisible by i, return i
        if n % i == 0:
            return i

# Example usage:
print(largest_divisor(15))  # Output: 5
print(largest_divisor(25))  # Output: 5
```

This script defines a function `largest_divisor` that takes an integer `n` and returns the largest number that divides `n` evenly, smaller than `n`. It uses a simple loop to start from `n-1` and check each number if it's a divisor of `n`. The loop stops when it finds the first number that satisfies this condition, which is the largest divisor of `n`.