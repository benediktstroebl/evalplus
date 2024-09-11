```python
def largest_divisor(n: int) -> int:
    """
    For a given number n, find the largest number that divides n evenly, smaller than n.

    Args:
    n (int): The input number.

    Returns:
    int: The largest number that divides n evenly, smaller than n.

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

This script defines a function `largest_divisor` that iterates over all numbers from `n-1` down to `1`, and returns the first number that divides `n` evenly. The test case `largest_divisor(15)` is also included to demonstrate the function's usage.