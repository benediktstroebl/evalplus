```python
def greatest_common_divisor(a: int, b: int) -> int:
    """
    Return a greatest common divisor of two integers a and b.

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
    while b:
        a, b = b, a % b
    return abs(a)

# Test cases
print(greatest_common_divisor(3, 5))  # Expected output: 1
print(greatest_common_divisor(25, 15))  # Expected output: 5
```

In this script, we use the Euclidean algorithm to find the greatest common divisor (GCD) of two integers `a` and `b`. The basic idea is that the GCD of `a` and `b` is the same as the GCD of `b` and the remainder of `a` divided by `b`. We repeat this process until `b` becomes zero, at which point `a` is the GCD.

We use the absolute value function `abs` to ensure that the GCD is always non-negative, even if the inputs are negative.