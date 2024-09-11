```python
def greatest_common_divisor(a: int, b: int) -> int:
    """
    Return the greatest common divisor of two integers a and b.

    The greatest common divisor (GCD) of two integers is the largest integer that divides each of the integers without a remainder.

    :param a: The first integer.
    :param b: The second integer.
    :return: The greatest common divisor of a and b.
    """

    # Base case: If either a or b is zero, the GCD is the other number.
    if b == 0:
        return a
    else:
        # Use the Euclidean algorithm to find the GCD.
        return greatest_common_divisor(b, a % b)


if __name__ == "__main__":
    # Test the function.
    print(greatest_common_divisor(3, 5))  # Output: 1
    print(greatest_common_divisor(25, 15))  # Output: 5
```

This script uses the Euclidean algorithm to find the greatest common divisor (GCD) of two integers. The Euclidean algorithm is an efficient method for computing the GCD of two numbers, and it works by repeatedly replacing the larger number with the remainder of dividing the larger number by the smaller number.