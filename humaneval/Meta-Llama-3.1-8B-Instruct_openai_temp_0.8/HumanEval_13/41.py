### Greatest Common Divisor (GCD) using Euclidean Algorithm
```python
def greatest_common_divisor(a: int, b: int) -> int:
    """
    Return the greatest common divisor of two integers a and b.

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

    # Base case: If b is zero, the GCD is a
    if b == 0:
        return a

    # Recursive case: Replace a with b and b with the remainder of a divided by b
    else:
        return greatest_common_divisor(b, a % b)


# Example usage:
print(greatest_common_divisor(3, 5))  # Output: 1
print(greatest_common_divisor(25, 15))  # Output: 5
```
This script uses the Euclidean algorithm, an efficient method for computing the GCD of two integers. It works by repeatedly replacing `a` with `b` and `b` with the remainder of `a` divided by `b`, until `b` is zero. At that point, `a` is the GCD of the original `a` and `b`.