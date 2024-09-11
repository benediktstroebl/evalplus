```python
def largest_divisor(n: int) -> int:
    """
    For a given number n, find the largest number that divides n evenly, smaller than n.

    Args:
    n (int): The input number.

    Returns:
    int: The largest divisor of n, smaller than n.

    Examples:
    >>> largest_divisor(15)
    5
    """
    for i in range(n - 1, 0, -1):
        if n % i == 0:
            return i

# Test the function
print(largest_divisor(15))  # Output: 5
print(largest_divisor(20))  # Output: 10
print(largest_divisor(13))  # Output: 1
```

This script defines the `largest_divisor` function, which iterates from `n - 1` down to `1` and returns the first number that divides `n` evenly (i.e., leaves no remainder). The function is then tested with a few examples to demonstrate its correctness.