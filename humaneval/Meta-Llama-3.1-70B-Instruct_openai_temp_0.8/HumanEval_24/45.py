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
    # Start checking from the largest possible divisor
    for i in range(n - 1, 0, -1):
        # If n is divisible by i
        if n % i == 0:
            # Return i as the largest divisor
            return i

# Test the function
print(largest_divisor(15))  # Output: 5
```

This script works by iterating from `n-1` down to `1`, checking each number to see if it divides `n` evenly (i.e., with a remainder of `0`). As soon as it finds such a number, it returns it as the largest divisor.