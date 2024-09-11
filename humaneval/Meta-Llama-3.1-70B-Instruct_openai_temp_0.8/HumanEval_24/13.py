```python
def largest_divisor(n: int) -> int:
    """
    For a given number n, find the largest number that divides n evenly, smaller than n.

    Args:
        n (int): The number to find the largest divisor for.

    Returns:
        int: The largest number that divides n evenly, smaller than n.

    Examples:
        >>> largest_divisor(15)
        5
    """
    # Start from n-1, since n can't be divided by itself
    for i in range(n - 1, 0, -1):
        # Check if n is divisible by i
        if n % i == 0:
            # If divisible, return i
            return i

# Test the function
print(largest_divisor(15))  # Output: 5
```

This script defines a function `largest_divisor` that takes an integer `n` as input and returns the largest number that divides `n` evenly, smaller than `n`. It uses a simple loop to check all numbers from `n-1` down to `1` and returns the first number that divides `n` evenly. The function includes a docstring that explains its purpose, parameters, return value, and provides an example usage.