```python
def largest_divisor(n: int) -> int:
    """
    For a given number n, find the largest number that divides n evenly, smaller than n

    Args:
    n (int): The number to find the largest divisor of.

    Returns:
    int: The largest divisor of n.

    Examples:
    >>> largest_divisor(15)
    5
    >>> largest_divisor(20)
    10
    """
    for i in range(n - 1, 0, -1):
        if n % i == 0:
            return i

# Example usage:
print(largest_divisor(15))  # Output: 5
print(largest_divisor(20))  # Output: 10
```
This script works by iterating from `n-1` down to `1`, and returning the first number that divides `n` evenly (i.e., with a remainder of `0`). This is the largest divisor of `n` that is smaller than `n`.