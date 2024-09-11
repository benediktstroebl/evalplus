```python
def largest_divisor(n: int) -> int:
    """
    For a given number n, find the largest number that divides n evenly, smaller than n.

    Args:
    n (int): The input number.

    Returns:
    int: The largest divisor of n.

    Example:
    >>> largest_divisor(15)
    5
    """
    # We start checking from n-1 down to 1
    for i in range(n-1, 0, -1):
        # If n is divisible by i, then i is the largest divisor
        if n % i == 0:
            return i

# Test the function
print(largest_divisor(15))  # Output: 5
print(largest_divisor(24))  # Output: 12
print(largest_divisor(31))  # Output: 1
```

This script defines the `largest_divisor` function, which uses a simple iterative approach to find the largest divisor of a given number `n`. It starts checking from `n-1` down to `1`, and returns the first number that divides `n` evenly. If no such number is found, it returns `1`, which is the smallest divisor of any number. The script also includes test cases to demonstrate the function's usage.