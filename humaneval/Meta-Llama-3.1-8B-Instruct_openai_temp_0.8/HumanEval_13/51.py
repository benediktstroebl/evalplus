```python
def greatest_common_divisor(a: int, b: int) -> int:
    """
    Return the greatest common divisor of two integers a and b.

    The greatest common divisor (GCD) of a and b is the largest number that divides both a and b without leaving a remainder.

    :param a: The first integer.
    :param b: The second integer.
    :return: The greatest common divisor of a and b.
    """
    # Use the Euclidean algorithm to find the GCD
    while b!= 0:
        # Replace 'a' with 'b' and 'b' with the remainder of 'a' divided by 'b'
        a, b = b, a % b
    return abs(a)


# Test cases
print(greatest_common_divisor(3, 5))  # Expected output: 1
print(greatest_common_divisor(25, 15))  # Expected output: 5
```

This script uses the Euclidean algorithm to find the greatest common divisor of two integers. The algorithm works by repeatedly replacing the larger number with the remainder of the division of the two numbers, until the remainder is zero. At that point, the non-zero number is the greatest common divisor.

The `abs` function is used to ensure that the result is always positive, even if the input numbers are negative. This is because the GCD is defined as the largest number that divides both numbers without leaving a remainder, which is the same regardless of the sign of the numbers.