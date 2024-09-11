```python
def greatest_common_divisor(a: int, b: int) -> int:
    """
    Return a greatest common divisor of two integers a and b

    The Euclidean algorithm is used to find the GCD of two numbers.
    This algorithm is based on the principle that the greatest common divisor of two numbers a and b
    is the same as the greatest common divisor of b and the remainder of a divided by b.

    Args:
        a (int): The first integer.
        b (int): The second integer.

    Returns:
        int: The greatest common divisor of a and b.

    Example:
        >>> greatest_common_divisor(3, 5)
        1
        >>> greatest_common_divisor(25, 15)
        5
    """
    while b:
        a, b = b, a % b
    return a
```

To test the function, you can call it with different values:

```python
print(greatest_common_divisor(3, 5))  # Outputs: 1
print(greatest_common_divisor(25, 15))  # Outputs: 5
```

This script defines a function `greatest_common_divisor` that takes two integers `a` and `b` as input and returns their greatest common divisor. The function uses the Euclidean algorithm to find the GCD, which is an efficient method for calculating the GCD of two numbers. The function is well-documented with a docstring that explains its purpose, usage, and provides examples.