```python
def greatest_common_divisor(a: int, b: int) -> int:
    """
    Return a greatest common divisor of two integers a and b

    The greatest common divisor (GCD) of two integers a and b is the largest positive integer that divides both a and b without leaving a remainder.

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
    while b:
        a, b = b, a % b
    return a


# Test the function
print(greatest_common_divisor(3, 5))  # Output: 1
print(greatest_common_divisor(25, 15))  # Output: 5
```

This script defines a function `greatest_common_divisor` that calculates the greatest common divisor of two integers using the Euclidean algorithm. The function returns the GCD of the two input integers. The test cases at the end demonstrate the function's usage.