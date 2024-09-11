```python
def largest_divisor(n: int) -> int:
    """
    For a given number n, find the largest number that divides n evenly, smaller than n

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
print(largest_divisor(24))  # Output: 12
print(largest_divisor(31))  # Output: 1
```

This script defines a function `largest_divisor` that takes an integer `n` as input and returns the largest number that divides `n` evenly, smaller than `n`. The function uses a simple loop to iterate from `n-1` down to `1`, checking each number to see if it divides `n` evenly. The first number that does is returned as the result.

Note that this function has a time complexity of O(n), which means it may not be efficient for large inputs. If you need a more efficient solution, you could use a more advanced algorithm or data structure.