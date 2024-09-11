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
    for i in range(n - 1, 0, -1):
        if n % i == 0:
            return i

# Test the function
print(largest_divisor(15))  # Output: 5
```

This script defines the `largest_divisor` function, which iterates from `n - 1` down to `1` and returns the first number that divides `n` evenly. The function includes a docstring with a description, arguments, return value, and an example.

You can run this script to test the `largest_divisor` function with different inputs.