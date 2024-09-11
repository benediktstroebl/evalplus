```python
def largest_divisor(n: int) -> int:
    """
    For a given number n, find the largest number that divides n evenly, smaller than n

    Args:
        n (int): The input number.

    Returns:
        int: The largest divisor of n, smaller than n.

    Examples:
        >>> largest_divisor(15)
        5
        >>> largest_divisor(20)
        10
    """
    for i in range(n - 1, 0, -1):
        if n % i == 0:
            return i

# Test the function
print(largest_divisor(15))  # Output: 5
print(largest_divisor(20))  # Output: 10
```

This script defines a function `largest_divisor(n)` that iterates from `n-1` down to `1` to find the largest number that divides `n` evenly. It returns the first number it finds that meets this condition.

The script also includes example use cases to demonstrate the function's usage and verify its correctness.