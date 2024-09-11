### Greatest Common Divisor (GCD) Calculation
#### Using the Euclidean Algorithm

```python
def greatest_common_divisor(a: int, b: int) -> int:
    """
    Return the greatest common divisor of two integers a and b.

    The GCD of two integers is the largest positive integer that divides both numbers
    without leaving a remainder.

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

    # If b is zero, the GCD is a
    if b == 0:
        return a

    # Otherwise, recursively apply the Euclidean algorithm
    else:
        return greatest_common_divisor(b, a % b)


# Example usage:
print(greatest_common_divisor(3, 5))  # Output: 1
print(greatest_common_divisor(25, 15))  # Output: 5
```

This script uses the Euclidean algorithm, which is an efficient method for calculating the GCD of two numbers. The algorithm works by repeatedly replacing `a` and `b` with `b` and the remainder of `a` divided by `b`, until `b` is zero. At that point, `a` is the GCD of the original `a` and `b`.