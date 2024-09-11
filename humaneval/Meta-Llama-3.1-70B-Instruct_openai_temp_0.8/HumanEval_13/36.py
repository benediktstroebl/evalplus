```python
def greatest_common_divisor(a: int, b: int) -> int:
    """
    Return a greatest common divisor of two integers a and b.

    This function uses the Euclidean algorithm to find the greatest common divisor.

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
if __name__ == "__main__":
    import doctest
    doctest.testmod()
```

This script defines a function `greatest_common_divisor` that takes two integers as input and returns their greatest common divisor using the Euclidean algorithm. The function includes a docstring that describes its purpose, parameters, and return value. It also includes example use cases. The script then tests the function using the `doctest` module.

You can run this script to test the function. If all tests pass, it will not output anything. If any tests fail, it will output an error message.