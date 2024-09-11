```python
def greatest_common_divisor(a: int, b: int) -> int:
    """
    Return a greatest common divisor of two integers a and b.

    This function uses the Euclidean algorithm, which is an efficient method
    for computing the greatest common divisor of two integers.

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
    return a

# Test the function
print(greatest_common_divisor(3, 5))  # Output: 1
print(greatest_common_divisor(25, 15))  # Output: 5
```

This script defines a function `greatest_common_divisor` that takes two integers `a` and `b` as input and returns their greatest common divisor. The function uses the Euclidean algorithm, which is a simple and efficient method for computing the greatest common divisor of two integers.

The script also includes a docstring that provides documentation for the function, including a description of what the function does, the arguments it takes, the return value, and some examples of how to use the function.

Finally, the script includes some test cases to demonstrate how the function works. The test cases print the greatest common divisor of the pairs of integers `(3, 5)` and `(25, 15)`, which are `1` and `5`, respectively.