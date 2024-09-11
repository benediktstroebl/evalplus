```python
def greatest_common_divisor(a: int, b: int) -> int:
    """
    Return a greatest common divisor of two integers a and b.

    The greatest common divisor (GCD) of two integers a and b is the largest positive
    integer that divides both a and b without leaving a remainder.

    This function uses the Euclidean algorithm, which is an efficient method for computing
    the GCD of two numbers.

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

    # Base case: if b is zero, the GCD is a
    if b == 0:
        return a
    
    # Recursive case: replace a with b and b with the remainder of a divided by b
    # This is the Euclidean algorithm
    else:
        return greatest_common_divisor(b, a % b)


# Test the function
print(greatest_common_divisor(3, 5))  # Should print: 1
print(greatest_common_divisor(25, 15))  # Should print: 5
```

This script defines a function `greatest_common_divisor` that uses the Euclidean algorithm to find the greatest common divisor of two integers `a` and `b`. The function then tests itself with the examples provided. The function's docstring explains its purpose, parameters, return value, and behavior.