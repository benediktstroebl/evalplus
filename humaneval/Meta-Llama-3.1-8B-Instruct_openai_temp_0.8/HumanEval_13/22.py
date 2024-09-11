```python
def greatest_common_divisor(a: int, b: int) -> int:
    """
    This function calculates the greatest common divisor (GCD) of two integers.

    The GCD is the largest number that divides both numbers without leaving a remainder.

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

    # Ensure a and b are positive integers
    a = abs(a)
    b = abs(b)

    # If both numbers are zero, the GCD is undefined, so return 0
    if a == 0 and b == 0:
        raise ValueError("GCD is undefined for both inputs being zero")

    # If one of the numbers is zero, the GCD is the other number
    if a == 0:
        return b
    if b == 0:
        return a

    # Use the Euclidean algorithm to find the GCD
    while b!= 0:
        a, b = b, a % b

    return a


# Test the function
print(greatest_common_divisor(3, 5))  # Expected output: 1
print(greatest_common_divisor(25, 15))  # Expected output: 5
```

In this code, the `greatest_common_divisor` function uses the Euclidean algorithm to find the GCD of two integers. The Euclidean algorithm is an efficient method for computing the GCD of two numbers, and it works by repeatedly replacing `a` and `b` with `b` and `a % b` until `b` becomes zero. At that point, `a` is the GCD.

This function also handles the edge cases where one or both of the inputs are zero, and it raises a `ValueError` if both inputs are zero.