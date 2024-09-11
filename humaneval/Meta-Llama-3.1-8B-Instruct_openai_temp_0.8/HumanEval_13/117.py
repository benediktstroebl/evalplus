```python
def greatest_common_divisor(a: int, b: int) -> int:
    """
    Return a greatest common divisor of two integers a and b

    The algorithm used is the Euclidean algorithm, which is an efficient method
    for calculating the greatest common divisor of two integers.

    Args:
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
    while b!= 0:
        # Swap a and b
        a, b = b, a % b
    return abs(a)


# Test the function
print(greatest_common_divisor(3, 5))  # Should print 1
print(greatest_common_divisor(25, 15))  # Should print 5
```

This script defines a function `greatest_common_divisor` that calculates the greatest common divisor (GCD) of two integers using the Euclidean algorithm. It then tests the function with a few examples.