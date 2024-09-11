```python
def greatest_common_divisor(a: int, b: int) -> int:
    """
    Return the greatest common divisor of two integers a and b.

    The function uses the Euclidean algorithm to find the GCD.

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
    # Recursive case: The GCD of a and b is the same as the GCD of b and the remainder of a divided by b
    else:
        return greatest_common_divisor(b, a % b)


# Test the function
print(greatest_common_divisor(3, 5))  # Output: 1
print(greatest_common_divisor(25, 15))  # Output: 5
```

This script defines a function `greatest_common_divisor` that takes two integers `a` and `b` as input and returns their greatest common divisor (GCD). The function uses the Euclidean algorithm, which is a popular method for calculating the GCD of two numbers. It does this by recursively replacing the larger number by its remainder when divided by the smaller number. The base case is when the second number `b` becomes zero, in which case the GCD is the first number `a`. The function then tests itself with two examples.