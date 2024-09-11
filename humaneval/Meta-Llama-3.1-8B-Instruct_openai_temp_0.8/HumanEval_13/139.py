### Greatest Common Divisor (GCD) in Python
#### Using the Euclidean Algorithm

```python
def greatest_common_divisor(a: int, b: int) -> int:
    """ Return the greatest common divisor of two integers a and b

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

    # If b is zero, a is the greatest common divisor
    while b:
        # Replace a with b and b with the remainder of a divided by b
        a, b = b, a % b

    return a

# Test the function
print(greatest_common_divisor(3, 5))  # Output: 1
print(greatest_common_divisor(25, 15))  # Output: 5
```

This script uses the Euclidean algorithm to find the greatest common divisor of two integers. The algorithm works by repeatedly replacing `a` with `b` and `b` with the remainder of `a` divided by `b`, until `b` is zero. At that point, `a` is the greatest common divisor of the original `a` and `b`.