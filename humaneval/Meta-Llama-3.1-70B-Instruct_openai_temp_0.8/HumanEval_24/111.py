```python
def largest_divisor(n: int) -> int:
    """
    For a given number n, find the largest number that divides n evenly, smaller than n

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

# Example usage
print(largest_divisor(15))  # Output: 5
print(largest_divisor(17))  # Output: 1
print(largest_divisor(24))  # Output: 12
```

This script defines a function `largest_divisor` that takes an integer `n` as input and returns the largest number that divides `n` evenly, smaller than `n`. It does this by iterating over all numbers from `n - 1` down to 1 and returning the first number that divides `n` evenly.

Note that the time complexity of this function is O(n), which can be inefficient for large inputs. If you need to handle large inputs, you could optimize this function to only iterate up to the square root of `n`, which would reduce the time complexity to O(sqrt(n)).