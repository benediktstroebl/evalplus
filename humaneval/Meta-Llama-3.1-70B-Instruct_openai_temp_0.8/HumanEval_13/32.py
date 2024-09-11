```python
def greatest_common_divisor(a: int, b: int) -> int:
    """
    Return a greatest common divisor of two integers a and b.

    This function uses the Euclidean algorithm to find the greatest common divisor.

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

    # Ensure a and b are positive
    a = abs(a)
    b = abs(b)

    # If b is zero, the GCD is a
    while b!= 0:
        # Replace a with b and b with the remainder of a divided by b
        a, b = b, a % b

    return a

# Test the function
print(greatest_common_divisor(3, 5))  # Should print 1
print(greatest_common_divisor(25, 15))  # Should print 5
```
This Python script defines a function called `greatest_common_divisor` that takes two integers `a` and `b` as input and returns their greatest common divisor. The function uses the Euclidean algorithm to find the GCD, which is a efficient method for computing the GCD of two integers. The script also includes example use cases and test cases to demonstrate how the function works.