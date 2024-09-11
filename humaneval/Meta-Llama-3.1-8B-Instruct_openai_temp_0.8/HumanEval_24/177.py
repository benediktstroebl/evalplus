```python
def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    Args:
        n (int): The number to find the largest divisor for.

    Returns:
        int: The largest number that divides n evenly, smaller than n.

    Examples:
        >>> largest_divisor(15)
        5
    """
    # Start from the number itself and decrease until we find a divisor
    for i in range(n, 1, -1):
        # Check if i is a divisor of n
        if n % i == 0:
            # If it is, return it as the largest divisor
            return i

# Test the function
print(largest_divisor(15))  # Should print 5
print(largest_divisor(20))  # Should print 20
print(largest_divisor(100))  # Should print 100
```

This script defines a function `largest_divisor` that takes an integer `n` and returns the largest number that divides `n` evenly, which is smaller than `n`. It uses a simple loop to check each number from `n` down to 2, returning the first number that is a divisor of `n`. The loop starts from `n` and decreases by 1 each time, thus ensuring that we find the largest divisor. The function includes docstrings that provide documentation and an example usage. The script then tests the function with a few examples.