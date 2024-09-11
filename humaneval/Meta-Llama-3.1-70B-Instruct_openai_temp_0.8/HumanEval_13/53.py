```python
def greatest_common_divisor(a: int, b: int) -> int:
    """
    Return a greatest common divisor of two integers a and b.

    This function uses the Euclidean algorithm, which is a well-known method for
    finding the greatest common divisor of two numbers.

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
        # The % operator returns the remainder of the division of a by b
        a, b = b, a % b
    return a

# Example use cases
print(greatest_common_divisor(3, 5))  # Output: 1
print(greatest_common_divisor(25, 15))  # Output: 5
print(greatest_common_divisor(48, 18))  # Output: 6
```

This script defines a function `greatest_common_divisor` that takes two integers `a` and `b` as arguments and returns their greatest common divisor. It uses the Euclidean algorithm, which repeatedly replaces `a` and `b` with `b` and the remainder of `a` divided by `b`, until `b` is zero. At that point, `a` is the greatest common divisor.