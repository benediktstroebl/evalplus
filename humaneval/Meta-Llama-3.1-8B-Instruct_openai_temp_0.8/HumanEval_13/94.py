```python
def greatest_common_divisor(a: int, b: int) -> int:
    """
    Return a greatest common divisor of two integers a and b.

    This function uses the Euclidean algorithm, which is a well-known method
    for calculating the GCD of two numbers. It works by repeatedly applying
    the identity gcd(a, b) = gcd(b, a % b) until b is zero, at which point
    a is the GCD.

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

    # Base case: if b is zero, a is the GCD
    while b!= 0:
        # Calculate the remainder of a divided by b
        a, b = b, a % b
    # Return the GCD
    return a

# Test the function
print(greatest_common_divisor(3, 5))  # Should print 1
print(greatest_common_divisor(25, 15))  # Should print 5
```

This script uses the Euclidean algorithm to calculate the greatest common divisor of two integers. It takes two integers as input, and returns their greatest common divisor. The function is well-documented with comments and doctests to illustrate its usage and behavior.