```python
def greatest_common_divisor(a: int, b: int) -> int:
    """
    Return a greatest common divisor of two integers a and b.

    The function uses the Euclidean algorithm to find the GCD.
    This algorithm is based on the principle that the greatest common divisor of two numbers
    does not change if the larger number is replaced by its difference with the smaller number.

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

    # Continue the loop until b is zero
    while b:
        # Swap a and b, and replace b with the remainder of a divided by b
        a, b = b, a % b

    # When b is zero, a is the GCD
    return a

# Test the function
print(greatest_common_divisor(3, 5))  # Output: 1
print(greatest_common_divisor(25, 15))  # Output: 5
```

This script uses the Euclidean algorithm to find the GCD of two numbers. The function takes two integers `a` and `b` as input, and returns their GCD. The algorithm works by repeatedly replacing the larger number with its difference with the smaller number, until the smaller number is zero. At this point, the larger number is the GCD.