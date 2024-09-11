```python
def largest_divisor(n: int) -> int:
    """ 
    For a given number n, find the largest number that divides n evenly, smaller than n
    
    Args:
    n (int): A positive integer.
    
    Returns:
    int: The largest divisor of n smaller than n.
    
    Raises:
    ValueError: If n is not a positive integer.
    
    Example:
    >>> largest_divisor(15)
    5
    """
    
    # Check if n is a positive integer
    if not isinstance(n, int) or n <= 0:
        raise ValueError("Input must be a positive integer.")
    
    # Start from n-1 and check for divisibility
    for i in range(n-1, 0, -1):
        # Check if i is a divisor of n
        if n % i == 0:
            # If i is a divisor, return it as the largest divisor
            return i

# Test the function
print(largest_divisor(15))  # Output: 5
print(largest_divisor(17))  # Output: 1 (since 17 is a prime number)
```

This script defines a function `largest_divisor` that takes an integer `n` as input and returns the largest number that divides `n` evenly, smaller than `n`. It checks each number from `n-1` down to 1 for divisibility, returning the first number it finds that is a divisor of `n`. The function also includes input validation to raise a `ValueError` if `n` is not a positive integer.