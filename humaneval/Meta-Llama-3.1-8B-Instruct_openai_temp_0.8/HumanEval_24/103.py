```python
def largest_divisor(n: int) -> int:
    """
    For a given number n, find the largest number that divides n evenly, smaller than n.

    Args:
    n (int): The input number.

    Returns:
    int: The largest divisor of n smaller than n.

    Examples:
    >>> largest_divisor(15)
    5
    """
    for i in range(n - 1, 0, -1):
        if n % i == 0:
            return i
    return 1  # In case n is a prime number or 1

# Test the function
print(largest_divisor(15))  # Output: 5
print(largest_divisor(17))  # Output: 1
print(largest_divisor(1))   # Output: 1
```

This script defines a function `largest_divisor` that finds the largest divisor of a given number `n` smaller than `n`. It does this by iterating over the numbers from `n-1` down to `1` and checking each number to see if it divides `n` evenly (i.e., `n % i == 0`). The first number it finds that does divide `n` evenly is returned as the largest divisor. If no such number is found, it returns `1`.