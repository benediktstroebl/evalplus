### Greatest Common Divisor (GCD) Script
```python
def greatest_common_divisor(a: int, b: int) -> int:
    """Return a greatest common divisor of two integers a and b.

    This function uses the Euclidean algorithm to find the GCD.
    It recursively divides the larger number by the smaller one until the remainder is 0.
    The GCD is the last non-zero remainder.

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
    # Base case: if b is 0, the GCD is a
    if b == 0:
        return a
    # Recursive case: find the GCD of b and the remainder of a divided by b
    else:
        return greatest_common_divisor(b, a % b)


# Test cases
print(greatest_common_divisor(3, 5))  # Output: 1
print(greatest_common_divisor(25, 15))  # Output: 5
```

This script uses the Euclidean algorithm to find the GCD of two integers. It works by dividing the larger number by the smaller one and taking the remainder. This process is repeated until the remainder is 0, at which point the GCD is the last non-zero remainder. The script includes test cases to demonstrate its usage.