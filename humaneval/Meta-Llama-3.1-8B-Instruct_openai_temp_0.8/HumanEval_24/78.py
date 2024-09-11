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


# Test the function
print(largest_divisor(15))  # Output: 5
print(largest_divisor(17))  # Output: 1 (because 1 is the only divisor of 17)
print(largest_divisor(20))  # Output: 20 (because 20 is the largest divisor of 20)
```

This script uses a simple loop to iterate from `n-1` down to `1`, checking each number to see if it's a divisor of `n` by using the modulo operator (`%`). The first number it finds that is a divisor is the largest one, because all larger divisors would have been checked and found not to be divisors.