```python
def greatest_common_divisor(a: int, b: int) -> int:
    """
    Return the greatest common divisor of two integers a and b.

    The greatest common divisor (GCD) of two integers is the largest integer
    that divides both numbers without leaving a remainder.

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
    while b!= 0:
        # Swap a and b
        a, b = b, a % b
    return abs(a)

# Example usage
print(greatest_common_divisor(3, 5))  # Output: 1
print(greatest_common_divisor(25, 15))  # Output: 5
```

In this script, the `greatest_common_divisor` function uses the Euclidean algorithm to find the GCD of two integers `a` and `b`. The algorithm works by repeatedly replacing `a` and `b` with `b` and the remainder of `a` divided by `b` until `b` is zero. At that point, `a` is the GCD.

The function takes two integers `a` and `b` as input and returns their GCD. It also includes documentation and example usage to demonstrate its usage.