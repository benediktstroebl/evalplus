```python
def greatest_common_divisor(a: int, b: int) -> int:
    """
    Return a greatest common divisor of two integers a and b

    The Euclidean algorithm is used to find the greatest common divisor.

    Args:
        a (int): The first integer
        b (int): The second integer

    Returns:
        int: The greatest common divisor of a and b

    Example:
        >>> greatest_common_divisor(3, 5)
        1
        >>> greatest_common_divisor(25, 15)
        5
    """
    while b!= 0:
        # Swap a and b, and replace b with the remainder of a divided by b
        a, b = b, a % b
    return abs(a)

# Test the function
print(greatest_common_divisor(3, 5))
print(greatest_common_divisor(25, 15))
```

This script uses the Euclidean algorithm to find the greatest common divisor of two integers. It repeatedly replaces `a` with `b` and `b` with the remainder of `a` divided by `b` until `b` is zero. At this point, `a` is the greatest common divisor.

The `abs` function is used to ensure that the result is always positive, as the greatest common divisor is a positive integer.