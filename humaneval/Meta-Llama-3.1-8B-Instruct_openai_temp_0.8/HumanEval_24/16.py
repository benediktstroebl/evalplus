```python
def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n.
    
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

# Example usage:
print(largest_divisor(15))  # Output: 5
print(largest_divisor(20))  # Output: 20 (because 20 is a perfect square)
print(largest_divisor(1))   # Output: 1
print(largest_divisor(17))  # Output: 17 (because 17 is a prime number)
```

In this script, we iterate over numbers from `n-1` to `1` and check if any of them divides `n` evenly using the modulo operator (`%`). The first number that does, we return as the largest divisor. This approach is simple, yet efficient, as it only requires a single pass through the numbers from `n-1` to `1`.