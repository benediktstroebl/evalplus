```python
def largest_divisor(n: int) -> int:
    """
    For a given number n, find the largest number that divides n evenly, smaller than n.

    Args:
    n (int): The input number.

    Returns:
    int: The largest divisor of n smaller than n.

    Example:
    >>> largest_divisor(15)
    5
    """
    for i in range(n - 1, 0, -1):
        if n % i == 0:
            return i

# Test the function
print(largest_divisor(15))  # Output: 5
print(largest_divisor(21))  # Output: 7
print(largest_divisor(30))  # Output: 15
```

This script defines a function `largest_divisor` that takes an integer `n` as input and returns the largest number smaller than `n` that divides `n` evenly. The function iterates from `n-1` down to `1` to find the first number that divides `n` with no remainder. This number is the largest divisor of `n` smaller than `n`. The script also includes some test cases to demonstrate the function's usage.