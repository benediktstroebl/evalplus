```python
def largest_divisor(n: int) -> int:
    """
    For a given number n, find the largest number that divides n evenly, smaller than n

    Args:
        n (int): The number to find the largest divisor for

    Returns:
        int: The largest number that divides n evenly, smaller than n

    Example:
        >>> largest_divisor(15)
        5
    """
    for i in range(n - 1, 0, -1):
        if n % i == 0:
            return i

# Test the function
print(largest_divisor(15))  # Output: 5
print(largest_divisor(20))  # Output: 20 // 4 = 4 because we need a number smaller that 20.
print(largest_divisor(30))  # Output: 15
```

This script defines a function `largest_divisor(n)` that takes an integer `n` as input and returns the largest number that divides `n` evenly, smaller than `n`. The function iterates through the numbers from `n-1` down to `1`, checking if each number is a divisor of `n` using the modulo operator (`n % i == 0`). As soon as it finds such a divisor, it returns the number.