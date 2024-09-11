```python
def greatest_common_divisor(a: int, b: int) -> int:
    """
    Return a greatest common divisor of two integers a and b.

    The greatest common divisor (GCD) of two integers is the largest integer 
    that divides both numbers without leaving a remainder.

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
    return abs(a)

# Test the function
print(greatest_common_divisor(3, 5))  # Expected output: 1
print(greatest_common_divisor(25, 15))  # Expected output: 5
```

This script uses the Euclidean algorithm to find the greatest common divisor of two integers. The Euclidean algorithm works by repeatedly replacing 'a' with 'b' and 'b' with the remainder of 'a' divided by 'b' until 'b' is zero. At that point, 'a' is the greatest common divisor. The `abs` function is used to ensure that the result is always non-negative, as the greatest common divisor is always non-negative.