```python
def greatest_common_divisor(a: int, b: int) -> int:
    """
    Return a greatest common divisor of two integers a and b.

    The greatest common divisor (GCD) of two integers is the largest positive integer
    that divides each of the integers without a remainder.

    Args:
    a (int): First integer.
    b (int): Second integer.

    Returns:
    int: The GCD of a and b.

    Examples:
    >>> greatest_common_divisor(3, 5)
    1
    >>> greatest_common_divisor(25, 15)
    5
    """

    # Use the Euclidean algorithm to find the GCD
    while b:
        a, b = b, a % b
    return a

# Test the function
print(greatest_common_divisor(3, 5))   # Expected output: 1
print(greatest_common_divisor(25, 15)) # Expected output: 5
```

This script uses the Euclidean algorithm to find the greatest common divisor of two integers. The algorithm works by repeatedly replacing 'a' and 'b' with 'b' and 'a % b' until 'b' is zero. At that point, 'a' is the GCD of the original 'a' and 'b'.