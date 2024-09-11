```python
def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    Args:
        n (int): The number to find the largest divisor for.

    Returns:
        int: The largest number that divides n evenly, smaller than n.

    Examples:
        >>> largest_divisor(15)
        5
    """
    # We start by checking if n is divisible by 2, then 3, and so on until the square root of n
    for i in range(n - 1, 1, -1):
        # Check if i is a divisor of n
        if n % i == 0:
            # If it is, return i as the largest divisor
            return i


# Example usage:
print(largest_divisor(15))  # Output: 5
print(largest_divisor(12))  # Output: 6
```

This script defines a function `largest_divisor(n)` that takes an integer `n` as input and returns the largest number that divides `n` evenly, smaller than `n`. It achieves this by iterating from `n-1` down to 2 and checking if each number is a divisor of `n`. If it finds a divisor, it immediately returns it as the largest divisor.