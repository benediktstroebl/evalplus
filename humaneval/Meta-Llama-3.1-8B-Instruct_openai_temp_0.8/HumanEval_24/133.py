```python
def largest_divisor(n: int) -> int:
    """
    For a given number n, find the largest number that divides n evenly, smaller than n.

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

# Test the function
print(largest_divisor(15))  # Output: 5
print(largest_divisor(16))  # Output: 8
print(largest_divisor(17))  # Output: 1
```

This function works by checking each number from `n-1` down to `1` to see if it divides `n` evenly. As soon as it finds a divisor, it returns that number. The loop starts from `n-1` because the problem states that the divisor should be smaller than `n`, and we can stop at `1` because the only number that divides any number is 1. If no divisor is found (which is not possible for any input), the function would return the first number it checks, which is `n-1`.