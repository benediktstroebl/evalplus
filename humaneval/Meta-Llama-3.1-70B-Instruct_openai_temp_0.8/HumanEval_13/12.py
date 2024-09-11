```python
def greatest_common_divisor(a: int, b: int) -> int:
    """
    Return a greatest common divisor of two integers a and b.

    This function uses the Euclidean algorithm to find the GCD of two numbers.

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

    # If b is 0, the GCD is a
    while b!= 0:
        # Replace a with b and b with the remainder of a divided by b
        a, b = b, a % b

    return a


# Test cases
print(greatest_common_divisor(3, 5))  # Expected output: 1
print(greatest_common_divisor(25, 15))  # Expected output: 5
```

This script defines a function `greatest_common_divisor` that takes two integers as input and returns their greatest common divisor (GCD). It uses the Euclidean algorithm to calculate the GCD. The script includes test cases to demonstrate its usage.