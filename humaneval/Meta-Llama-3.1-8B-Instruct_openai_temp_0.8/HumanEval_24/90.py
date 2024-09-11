```python
def largest_divisor(n: int) -> int:
    """
    For a given number n, find the largest number that divides n evenly, smaller than n

    Args:
        n (int): The input number

    Returns:
        int: The largest divisor of n

    Examples:
        >>> largest_divisor(15)
        5
    """
    for i in range(n - 1, 0, -1):
        if n % i == 0:
            return i

# Example usage:
print(largest_divisor(15))  # Output: 5
print(largest_divisor(20))  # Output: 20 (since the largest divisor of 20 is 20 itself)
print(largest_divisor(13))  # Output: 1 (since the largest divisor of 13 is 1)
```

This script uses a simple loop to iterate from `n-1` down to 1, checking each number to see if it is a divisor of `n` by using the modulo operator (`%`). If it finds a divisor, it immediately returns that value.