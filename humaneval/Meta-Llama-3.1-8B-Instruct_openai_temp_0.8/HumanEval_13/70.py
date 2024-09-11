### Greatest Common Divisor (GCD) Calculator
#### Using the Euclidean Algorithm

```python
def greatest_common_divisor(a: int, b: int) -> int:
    """
    Return a greatest common divisor of two integers a and b.

    The GCD is the largest positive integer that divides both numbers without leaving a remainder.

    :param a: The first integer.
    :param b: The second integer.
    :return: The greatest common divisor of a and b.
    """

    # Ensure a and b are positive integers
    a = abs(a)
    b = abs(b)

    # If b is zero, the GCD is a
    while b:
        a, b = b, a % b

    return a

# Example usage:
print(greatest_common_divisor(3, 5))     # Output: 1
print(greatest_common_divisor(25, 15))  # Output: 5
```

This script uses the Euclidean algorithm to calculate the greatest common divisor (GCD) of two integers. The algorithm works by repeatedly replacing `a` and `b` with `b` and the remainder of `a` divided by `b`, until `b` is zero. At this point, `a` is the GCD of the original `a` and `b`.