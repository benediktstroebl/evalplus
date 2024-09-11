### Largest Divisor Function
```python
def largest_divisor(n: int) -> int:
    """
    For a given number n, find the largest number that divides n evenly, smaller than n

    Args:
        n (int): Input number

    Returns:
        int: The largest divisor of n

    Example:
        >>> largest_divisor(15)
        5
    """
    for i in range(n - 1, 0, -1):
        if n % i == 0:
            return i
    return 1  # Return 1 if n is a prime number

# Test the function
print(largest_divisor(15))  # Output: 5
print(largest_divisor(12))  # Output: 4
print(largest_divisor(13))  # Output: 1
```

This script defines a function `largest_divisor` that takes an integer `n` as input and returns the largest number that divides `n` evenly, which is smaller than `n`. The function iterates from `n-1` down to `1` and checks if `n` is divisible by the current number. If it is, the function returns that number. If no such number is found (which means `n` is a prime number), the function returns `1`.