### Largest Divisor Function
```python
def largest_divisor(n: int) -> int:
    """
    For a given number n, find the largest number that divides n evenly, smaller than n.
    
    Args:
        n (int): The number for which to find the largest divisor.
    
    Returns:
        int: The largest divisor of n.
    
    Example:
        >>> largest_divisor(15)
        5
    """
    # We start from n-1 and check each number if it's a divisor of n
    for i in range(n-1, 0, -1):
        # If n is divisible by i, return i as the largest divisor
        if n % i == 0:
            return i

# Test the function
print(largest_divisor(15))  # Output: 5
print(largest_divisor(10))  # Output: 5
print(largest_divisor(17))  # Output: 1
```
This script uses a simple loop to check each number smaller than n to see if it's a divisor. It starts from `n-1` and goes down to 1, so the first number it checks that's a divisor will be the largest.