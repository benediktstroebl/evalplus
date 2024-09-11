```python
def largest_divisor(n: int) -> int:
    """
    For a given number n, find the largest number that divides n evenly, smaller than n.
    
    Args:
        n (int): The input number.
    
    Returns:
        int: The largest divisor of n, smaller than n.
    
    Example:
        >>> largest_divisor(15)
        5
    """
    # Start checking from the largest possible divisor, which is n-1
    for i in range(n-1, 0, -1):
        # Check if i is a divisor of n
        if n % i == 0:
            # If i is a divisor, return it as the largest divisor
            return i

# Test the function
print(largest_divisor(15))  # Output: 5
```