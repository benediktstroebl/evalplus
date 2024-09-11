```python
def greatest_common_divisor(a: int, b: int) -> int:
    """
    Return a greatest common divisor of two integers a and b

    Args:
        a (int): The first integer.
        b (int): The second integer.

    Returns:
        int: The greatest common divisor of a and b.

    Example:
        >>> greatest_common_divisor(3, 5)
        1
        >>> greatest_common_divisor(25, 15)
        5
    """

    # Use the Euclidean algorithm to find the GCD
    while b!= 0:
        a, b = b, a % b

    return abs(a)


# Test the function
print(greatest_common_divisor(3, 5))  # Output: 1
print(greatest_common_divisor(25, 15))  # Output: 5
```

This script defines a function `greatest_common_divisor(a, b)` that takes two integers `a` and `b` as input and returns their greatest common divisor using the Euclidean algorithm. The algorithm repeatedly replaces `a` with `b` and `b` with the remainder of `a` divided by `b` until `b` is zero, at which point `a` is the greatest common divisor. The function then returns the absolute value of `a`. The script includes docstrings and example use cases to illustrate the function's behavior.