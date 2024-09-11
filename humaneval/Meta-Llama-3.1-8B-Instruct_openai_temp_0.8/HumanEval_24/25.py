```python
def largest_divisor(n: int) -> int:
    """
    For a given number n, find the largest number that divides n evenly, smaller than n.

    Args:
        n (int): The input number.

    Returns:
        int: The largest divisor of n.

    Examples:
        >>> largest_divisor(15)
        5
    """
    for i in range(n - 1, 0, -1):
        if n % i == 0:
            return i
    return 1  # If n is a prime number, return 1 as the largest divisor

# Example usage:
print(largest_divisor(15))  # Output: 5
print(largest_divisor(17))  # Output: 1
```

This script defines a function `largest_divisor` that takes an integer `n` as input and returns its largest divisor smaller than `n`. It uses a simple loop to iterate from `n - 1` down to `1` (or `n - 2` if `n` is even) to find the first number that divides `n` evenly. If no such number is found (i.e., if `n` is a prime number), it returns `1`.