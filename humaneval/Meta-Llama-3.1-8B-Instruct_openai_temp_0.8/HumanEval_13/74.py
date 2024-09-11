```python
def greatest_common_divisor(a: int, b: int) -> int:
    """
    Return the greatest common divisor of two integers a and b.

    The Euclidean algorithm is used to efficiently calculate the GCD.
    This algorithm works by repeatedly replacing `a` and `b` with `b` and the remainder of `a` divided by `b`,
    until `b` is zero. At this point, `a` is the GCD.

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
        # Replace a with b and b with the remainder of a divided by b
        a, b = b, a % b
    return abs(a)  # Return the absolute value of the GCD


# Test the function
print(greatest_common_divisor(3, 5))  # Output: 1
print(greatest_common_divisor(25, 15))  # Output: 5
```

This script defines a function `greatest_common_divisor(a, b)` that takes two integers `a` and `b` as input and returns their greatest common divisor (GCD). It uses the Euclidean algorithm to efficiently calculate the GCD. The function includes docstrings with examples and explanations of how it works.