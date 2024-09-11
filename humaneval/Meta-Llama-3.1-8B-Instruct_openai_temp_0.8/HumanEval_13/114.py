```python
def greatest_common_divisor(a: int, b: int) -> int:
    """
    Return a greatest common divisor of two integers a and b

    Parameters:
    a (int): The first integer
    b (int): The second integer

    Returns:
    int: The greatest common divisor of a and b

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

This script uses the Euclidean algorithm to find the greatest common divisor of two integers `a` and `b`. The algorithm works by repeatedly applying the formula `a, b = b, a % b` until `b` is zero, at which point `a` is the greatest common divisor. The `abs` function is used to ensure that the result is always non-negative, even if the input numbers are negative.