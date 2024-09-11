```python
def largest_divisor(n: int) -> int:
    """
    For a given number n, find the largest number that divides n evenly, smaller than n

    Args:
        n (int): The number to find the largest divisor of.

    Returns:
        int: The largest divisor of n.

    >>> largest_divisor(15)
    5
    """
    for i in range(n - 1, 0, -1):
        if n % i == 0:
            return i

# Test the function
print(largest_divisor(15))  # Output: 5
```

This script defines a function `largest_divisor` that takes an integer `n` as input and returns the largest number that divides `n` evenly, smaller than `n`. It uses a simple loop to iterate from `n - 1` down to `1`, checking if each number is a divisor of `n` by using the modulus operator (`%`). As soon as it finds a divisor, it returns that number.