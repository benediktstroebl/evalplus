```python
def largest_divisor(n: int) -> int:
    """
    For a given number n, find the largest number that divides n evenly, smaller than n

    Args:
    n (int): The number to find the largest divisor of.

    Returns:
    int: The largest number that divides n evenly, smaller than n.

    Examples:
    >>> largest_divisor(15)
    5
    """
    for i in range(n - 1, 0, -1):
        if n % i == 0:
            return i

# Test the function
print(largest_divisor(15))  # Output: 5
print(largest_divisor(17))  # Output: 1
print(largest_divisor(24))  # Output: 12
```

This script works by iterating over all numbers smaller than `n` in descending order, and returning the first one that divides `n` evenly (i.e., with no remainder). The `range(n - 1, 0, -1)` function generates this sequence of numbers. The `if n % i == 0:` condition checks whether `i` divides `n` evenly.