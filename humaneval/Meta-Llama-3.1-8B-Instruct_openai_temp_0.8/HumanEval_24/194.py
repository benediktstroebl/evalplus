```python
def largest_divisor(n: int) -> int:
    """
    For a given number n, find the largest number that divides n evenly, smaller than n.

    Args:
        n (int): The input number.

    Returns:
        int: The largest divisor of n.

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

This script defines a function `largest_divisor` that finds the largest divisor of a given number `n`. It iterates from `n-1` down to `1` and returns the first number it finds that divides `n` evenly (i.e., the remainder is `0`). The example usage demonstrates the function's behavior with the input `15`, which has a largest divisor of `5`.