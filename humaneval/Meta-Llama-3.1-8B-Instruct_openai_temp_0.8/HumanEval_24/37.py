```python
def largest_divisor(n: int) -> int:
    """
    For a given number n, find the largest number that divides n evenly, smaller than n
    
    Args:
        n (int): A positive integer
    
    Returns:
        int: The largest divisor of n that is smaller than n
    
    Raises:
        ValueError: If n is not a positive integer
    
    >>> largest_divisor(15)
    5
    """
    if not isinstance(n, int) or n <= 0:
        raise ValueError("Input must be a positive integer")
    
    # Start from the second largest number (n-1) and find the first number that divides n evenly
    for i in range(n-1, 0, -1):
        if n % i == 0:
            return i

# Example usage
print(largest_divisor(15))  # Output: 5
print(largest_divisor(16))  # Output: 8
print(largest_divisor(25))  # Output: 5
```

This script defines a function `largest_divisor(n)` that finds the largest number that divides `n` evenly and returns it. It uses a for loop starting from `n-1` and going down to 1, and as soon as it finds a number that divides `n` evenly (i.e., `n % i == 0`), it returns that number. If `n` is not a positive integer, it raises a `ValueError`. The example usage at the end demonstrates how to use this function with different inputs.