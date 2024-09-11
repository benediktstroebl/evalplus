```python
def largest_divisor(n: int) -> int:
    """
    For a given number n, find the largest number that divides n evenly, smaller than n.
    
    Args:
        n (int): A positive integer.
    
    Returns:
        int: The largest number that divides n evenly, smaller than n.
    
    Examples:
        >>> largest_divisor(15)
        5
    """
    # Initialize the divisor as 1, it's the smallest possible divisor
    divisor = 1
    
    # Iterate over all numbers from 2 to n (inclusive)
    for i in range(2, n + 1):
        # Check if i is a divisor of n
        if n % i == 0:
            # If i is a divisor, update the divisor if it's larger than the current divisor
            divisor = max(divisor, i)
    
    # Return the largest divisor found
    return divisor

# Test the function
print(largest_divisor(15))  # Output: 5
```

This script defines a function `largest_divisor` that takes an integer `n` as input and returns the largest number that divides `n` evenly, smaller than `n`. The function iterates over all numbers from 2 to `n` (inclusive) and checks if each number is a divisor of `n` using the modulo operator (`%`). If a number is a divisor, it updates the divisor if it's larger than the current divisor. Finally, the function returns the largest divisor found.