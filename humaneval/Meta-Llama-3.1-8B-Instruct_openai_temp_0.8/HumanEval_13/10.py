```python
def greatest_common_divisor(a: int, b: int) -> int:
    """
    Return the greatest common divisor of two integers a and b.

    This function uses the Euclidean algorithm, which is a efficient method
    for computing the greatest common divisor of two integers.

    Args:
        a: The first integer.
        b: The second integer.

    Returns:
        The greatest common divisor of a and b.

    Example:
        >>> greatest_common_divisor(3, 5)
        1
        >>> greatest_common_divisor(25, 15)
        5
    """

    # Use the Euclidean algorithm to compute the GCD
    while b:
        a, b = b, a % b

    return abs(a)

# Test the function
print(greatest_common_divisor(3, 5))   # Expected output: 1
print(greatest_common_divisor(25, 15))  # Expected output: 5
```

This script uses the Euclidean algorithm, which is a well-known method for computing the greatest common divisor of two integers. It works by repeatedly applying the formula `gcd(a, b) = gcd(b, a % b)` until `b` is zero, at which point `a` is the greatest common divisor. The `abs` function is used to ensure that the result is always positive, even if `a` and `b` are negative.