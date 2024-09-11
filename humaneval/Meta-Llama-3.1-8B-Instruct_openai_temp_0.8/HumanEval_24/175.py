```python
def largest_divisor(n: int) -> int:
    """
    For a given number n, find the largest number that divides n evenly, smaller than n

    Args:
        n (int): The input number.

    Returns:
        int: The largest divisor of n smaller than n.

    Examples:
        >>> largest_divisor(15)
        5
    """
    for i in range(n - 1, 0, -1):
        if n % i == 0:
            return i

# Testing the function
print(largest_divisor(15))  # Output: 5
print(largest_divisor(10))  # Output: 5
print(largest_divisor(7))   # Output: 1
print(largest_divisor(16))  # Output: 8
```

This script defines a function `largest_divisor` that takes an integer `n` as input and returns the largest number that divides `n` evenly and is smaller than `n`. The function uses a loop to iterate from `n-1` down to `1`, checking if `n` is divisible by the current number. The first such number it finds is the largest divisor smaller than `n`, which is then returned.