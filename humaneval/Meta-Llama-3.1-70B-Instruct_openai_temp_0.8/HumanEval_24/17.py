```python
def largest_divisor(n: int) -> int:
    """
    For a given number n, find the largest number that divides n evenly, smaller than n.

    Args:
        n (int): The number to find the largest divisor of.

    Returns:
        int: The largest number that divides n evenly, smaller than n.

    Example:
        >>> largest_divisor(15)
        5
    """
    # We start from n-1 because the problem states the divisor should be smaller than n
    for i in range(n - 1, 0, -1):
        # If n is divisible by i, it means i is a divisor of n
        if n % i == 0:
            # Since we're iterating in descending order, the first divisor we find will be the largest
            return i

# Test the function
print(largest_divisor(15))  # Output: 5
```

This script defines a function `largest_divisor` that takes an integer `n` as input and returns the largest number that divides `n` evenly, smaller than `n`. It does this by iterating from `n-1` down to `1` and checking if `n` is divisible by each number. The first number it finds that divides `n` evenly will be the largest divisor, since the iteration is in descending order.