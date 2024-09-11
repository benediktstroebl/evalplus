```python
def largest_divisor(n: int) -> int:
    """
    For a given number n, find the largest number that divides n evenly, smaller than n.

    Args:
    n (int): The input number.

    Returns:
    int: The largest divisor of n.

    >>> largest_divisor(15)
    5
    """
    for i in range(n - 1, 0, -1):
        if n % i == 0:
            return i

# Example usage:
print(largest_divisor(15))  # Output: 5
print(largest_divisor(20))  # Output: 10
print(largest_divisor(31))  # Output: 1
```

This script defines the `largest_divisor` function as requested, along with a docstring that explains its purpose and provides example usage. The function works by iterating over all numbers from `n-1` down to 1, and returns the first number that divides `n` evenly. The script then includes some example usage to demonstrate how the function works.