```python
def largest_divisor(n: int) -> int:
    """
    For a given number n, find the largest number that divides n evenly, smaller than n

    Args:
        n (int): The input number.

    Returns:
        int: The largest divisor of n, smaller than n.

    Raises:
        ValueError: If n is less than 2.

    Examples:
        >>> largest_divisor(15)
        5
        >>> largest_divisor(17)
        1
    """
    if n < 2:
        raise ValueError("Input number should be greater than 1")

    for i in range(n - 1, 1, -1):
        if n % i == 0:
            return i

    return 1

# Test the function
print(largest_divisor(15))  # Output: 5
print(largest_divisor(17))  # Output: 1
```

This script defines a function `largest_divisor` that takes an integer `n` as input and returns the largest number that divides `n` evenly, smaller than `n`. The function iterates from `n - 1` down to `2` and checks if `n` is divisible by each number. If `n` is divisible by a number, that number is returned as the largest divisor. If no divisors are found, the function returns `1`, which is the divisor of every number.

The script also includes a test case to verify that the function works correctly.