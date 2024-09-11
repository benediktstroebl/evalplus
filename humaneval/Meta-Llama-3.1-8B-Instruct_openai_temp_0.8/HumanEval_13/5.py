Here's the Python script that solves the problem:
```markdown
### Greatest Common Divisor

This script uses the Euclidean algorithm to calculate the greatest common divisor (GCD) of two integers.

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
    while b:
        a, b = b, a % b
    return abs(a)


# Test cases
print(greatest_common_divisor(3, 5))  # Output: 1
print(greatest_common_divisor(25, 15))  # Output: 5
```

In this script, the `greatest_common_divisor` function uses the Euclidean algorithm to recursively find the greatest common divisor of two integers. The algorithm works by replacing `a` and `b` with `b` and the remainder of `a` divided by `b` until `b` is zero. At that point, `a` is the greatest common divisor. The `abs` function is used to ensure the result is always positive.