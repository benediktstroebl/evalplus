```python
def largest_divisor(n: int) -> int:
    """
    For a given number n, find the largest number that divides n evenly, smaller than n.

    Args:
        n (int): The input number.

    Returns:
        int: The largest divisor of n that is smaller than n.

    Examples:
        >>> largest_divisor(15)
        5
    """
    # Start checking from n-1, because n itself is not a valid divisor
    for i in range(n-1, 0, -1):
        # Check if i is a divisor of n
        if n % i == 0:
            # If it is, return i as the largest divisor
            return i

# Test the function
print(largest_divisor(15))  # Should print 5
print(largest_divisor(17))  # Should print 1
print(largest_divisor(24))  # Should print 12
```