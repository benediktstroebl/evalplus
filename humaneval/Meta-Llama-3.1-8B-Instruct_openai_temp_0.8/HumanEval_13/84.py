### Greatest Common Divisor (GCD) Calculator in Python
```python
def greatest_common_divisor(a: int, b: int) -> int:
    """
    Return a greatest common divisor of two integers a and b

    Args:
        a (int): The first integer
        b (int): The second integer

    Returns:
        int: The greatest common divisor of a and b

    Examples:
        >>> greatest_common_divisor(3, 5)
        1
        >>> greatest_common_divisor(25, 15)
        5
    """
    # Use the Euclidean algorithm to find the GCD
    while b:
        a, b = b, a % b
    return a

# Test the function
print(greatest_common_divisor(3, 5))  # Output: 1
print(greatest_common_divisor(25, 15))  # Output: 5
```
This script uses the Euclidean algorithm to calculate the greatest common divisor of two integers. The algorithm works by repeatedly replacing `a` and `b` with `b` and the remainder of `a` divided by `b`, until `b` is zero. At that point, `a` is the greatest common divisor.