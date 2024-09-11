### Greatest Common Divisor (GCD) Calculator
#### Using Euclid's Algorithm

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
    # If b is 0, the GCD is a (by definition)
    if b == 0:
        return a
    # Otherwise, recursively call the function with b and the remainder of a divided by b
    else:
        return greatest_common_divisor(b, a % b)


# Test the function
print(greatest_common_divisor(3, 5))  # Output: 1
print(greatest_common_divisor(25, 15))  # Output: 5
```

This script implements Euclid's algorithm to calculate the greatest common divisor (GCD) of two integers `a` and `b`. The function recursively calls itself with `b` and the remainder of `a` divided by `b`, until `b` becomes 0. At that point, `a` is the GCD.