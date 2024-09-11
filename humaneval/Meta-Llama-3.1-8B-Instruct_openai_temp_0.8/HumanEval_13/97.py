```python
def greatest_common_divisor(a: int, b: int) -> int:
    """
    Return a greatest common divisor of two integers a and b

    The function uses the Euclidean algorithm to find the greatest common divisor.

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

    # Use the Euclidean algorithm to find the greatest common divisor
    while b!= 0:
        a, b = b, a % b

    # The greatest common divisor is the last non-zero remainder
    return abs(a)


# Test cases
print(greatest_common_divisor(3, 5))  # Expected output: 1
print(greatest_common_divisor(25, 15))  # Expected output: 5
```

This script defines a function `greatest_common_divisor` that uses the Euclidean algorithm to find the greatest common divisor of two integers. The function takes two integers `a` and `b` as input and returns their greatest common divisor. The test cases at the end of the script demonstrate the function's usage and expected output.