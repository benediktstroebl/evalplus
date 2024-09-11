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
    >>> largest_divisor(17)
    1
    """
    for i in range(n - 1, 0, -1):
        if n % i == 0:
            return i

# Test the function
print(largest_divisor(15))  # Expected output: 5
print(largest_divisor(17))  # Expected output: 1
```

This script defines a function `largest_divisor(n)` that takes an integer `n` as input and returns the largest number that divides `n` evenly, smaller than `n`. It does this by iterating over numbers from `n-1` down to 1 and checking if `n` divided by the current number leaves a remainder of 0. If it does, it returns the current number as the largest divisor.

Note: This solution has a time complexity of O(n), which is not very efficient for large numbers. If you need to find the largest divisor for large numbers, a more efficient algorithm would be to iterate up to the square root of `n`, not `n` itself.