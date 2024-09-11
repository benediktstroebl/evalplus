```python
def greatest_common_divisor(a: int, b: int) -> int:
    """
    Return the greatest common divisor of two integers a and b.

    This function uses the Euclidean algorithm, which is an efficient method
    for computing the greatest common divisor of two integers.

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
    while b!= 0:
        # Swap the values of a and b, and replace b with the remainder of a divided by b
        a, b = b, a % b
    return abs(a)


# Test cases
print(greatest_common_divisor(3, 5))  # Expected output: 1
print(greatest_common_divisor(25, 15))  # Expected output: 5
```

This script uses the Euclidean algorithm to calculate the greatest common divisor of two integers. It works by continuously replacing `a` with `b` and `b` with the remainder of `a` divided by `b`, until `b` is 0. At that point, `a` is the greatest common divisor. The `abs` function is used to return a positive value, in case the input numbers have different signs.