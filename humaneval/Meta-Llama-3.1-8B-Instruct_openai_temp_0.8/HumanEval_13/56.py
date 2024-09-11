```python
def greatest_common_divisor(a: int, b: int) -> int:
    """
    Return the greatest common divisor of two integers a and b.

    This function uses the Euclidean algorithm, which is an efficient method for computing the GCD of two numbers.
    
    Args:
        a (int): The first integer.
        b (int): The second integer.

    Returns:
        int: The greatest common divisor of a and b.

    Examples:
        >>> greatest_common_divisor(3, 5)
        1
        >>> greatest_common_divisor(25, 15)
        5
    """
    while b:
        a, b = b, a % b
    return abs(a)


# Test cases
print(greatest_common_divisor(3, 5))  # Output: 1
print(greatest_common_divisor(25, 15))  # Output: 5
print(greatest_common_divisor(-10, 15))  # Output: 5
```

This script uses the Euclidean algorithm to calculate the greatest common divisor of two numbers. It repeatedly replaces `a` and `b` with `b` and the remainder of `a` divided by `b`, until `b` is zero. At that point, `a` is the GCD. The `abs` function is used to ensure the result is always positive, since the GCD is defined to be positive.