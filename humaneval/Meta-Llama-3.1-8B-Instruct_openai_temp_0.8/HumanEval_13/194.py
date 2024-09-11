### Greatest Common Divisor (GCD) in Python
```python
def greatest_common_divisor(a: int, b: int) -> int:
    """
    Return a greatest common divisor of two integers a and b

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
    # Use the Euclidean algorithm to find the GCD
    while b!= 0:
        a, b = b, a % b
    return abs(a)

# Test the function
print(greatest_common_divisor(3, 5))  # Output: 1
print(greatest_common_divisor(25, 15))  # Output: 5
```
This script uses the Euclidean algorithm to find the greatest common divisor of two integers `a` and `b`. The algorithm works by repeatedly replacing `a` and `b` with `b` and the remainder of `a` divided by `b` until `b` is 0. At this point, `a` is the greatest common divisor of the original `a` and `b`. The `abs` function is used to ensure the result is positive, regardless of the signs of the input integers.