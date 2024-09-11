```python
def largest_divisor(n: int) -> int:
    """
    For a given number n, find the largest number that divides n evenly, smaller than n.

    Args:
        n (int): The input number.

    Returns:
        int: The largest divisor of n smaller than n.

    Example:
        >>> largest_divisor(15)
        5
    """
    for i in range(n - 1, 0, -1):
        if n % i == 0:
            return i

# Test the function
print(largest_divisor(15))  # Output: 5
print(largest_divisor(10))  # Output: 5
print(largest_divisor(17))  # Output: 1
```

This script works by iterating over all numbers smaller than `n` in descending order, and returning the first one that divides `n` evenly. The `%` operator in Python returns the remainder of the division, so `n % i == 0` checks whether `i` divides `n` evenly.