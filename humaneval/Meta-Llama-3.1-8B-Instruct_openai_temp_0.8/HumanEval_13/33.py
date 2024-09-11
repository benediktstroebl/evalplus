```python
def greatest_common_divisor(a: int, b: int) -> int:
    """
    Return a greatest common divisor of two integers a and b

    The algorithm used is the Euclidean algorithm.

    Args:
        a (int): First integer
        b (int): Second integer

    Returns:
        int: Greatest common divisor of a and b

    Examples:
        >>> greatest_common_divisor(3, 5)
        1
        >>> greatest_common_divisor(25, 15)
        5
    """
    while b!= 0:
        # Use the modulo operator to get the remainder of a divided by b
        a, b = b, a % b
    return abs(a)

# Test the function
print(greatest_common_divisor(3, 5))  # Expected output: 1
print(greatest_common_divisor(25, 15))  # Expected output: 5
```

This script implements the Euclidean algorithm to calculate the greatest common divisor of two integers. The Euclidean algorithm is a simple method for calculating the greatest common divisor of two integers, and it's based on the principle that the greatest common divisor of two numbers does not change if the larger number is replaced by its difference with the smaller number. The algorithm continues until the remainder is zero, at which point the non-zero number is the greatest common divisor.