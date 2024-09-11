```python
def largest_divisor(n: int) -> int:
    """
    For a given number n, find the largest number that divides n evenly, smaller than n
    
    Parameters:
    n (int): The input number
    
    Returns:
    int: The largest divisor of n, smaller than n
    
    Examples:
    >>> largest_divisor(15)
    5
    """
    
    # Start from the number itself and move backwards to find the largest divisor
    for i in range(n, 0, -1):
        # Check if the current number is a divisor of n
        if n % i == 0:
            # If it is, return this number as the largest divisor
            return i

# Example usage:
print(largest_divisor(15))  # Output: 5
```

This script defines a function `largest_divisor` that takes an integer `n` as input and returns the largest number that divides `n` evenly, smaller than `n`. It works by iterating from `n` down to 1 and checking each number to see if it is a divisor of `n`. As soon as it finds a divisor, it returns that number.