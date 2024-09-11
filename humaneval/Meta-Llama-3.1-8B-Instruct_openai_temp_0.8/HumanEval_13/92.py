### Greatest Common Divisor Implementation

```python
def greatest_common_divisor(a: int, b: int) -> int:
    """
    Return a greatest common divisor of two integers a and b.

    The function uses the Euclidean algorithm to find the GCD.

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
print(greatest_common_divisor(3, 5))  # Expected output: 1
print(greatest_common_divisor(25, 15))  # Expected output: 5
print(greatest_common_divisor(-3, 5))  # Expected output: 1
print(greatest_common_divisor(25, -15))  # Expected output: 5
```

This script defines a function `greatest_common_divisor` that calculates the greatest common divisor of two integers `a` and `b` using the Euclidean algorithm. The function iteratively replaces `a` and `b` with `b` and the remainder of `a` divided by `b` until `b` becomes zero. At this point, `a` is the greatest common divisor. The `abs` function is used to ensure the result is always positive, regardless of the sign of the input integers. The script also includes test cases to demonstrate its usage.