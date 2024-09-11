```python
def greatest_common_divisor(a: int, b: int) -> int:
    """
    Return a greatest common divisor of two integers a and b

    This function uses the Euclidean algorithm to find the GCD of two numbers.
    The Euclidean algorithm is an efficient method for computing the greatest
    common divisor (GCD) of two integers.

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
    # Use the Euclidean algorithm to find the GCD
    while b!= 0:
        a, b = b, a % b
    return abs(a)


# Test the function
print(greatest_common_divisor(3, 5))  # Expected output: 1
print(greatest_common_divisor(25, 15))  # Expected output: 5
```

This script defines a function `greatest_common_divisor` that takes two integers `a` and `b` as input and returns their greatest common divisor (GCD). It uses the Euclidean algorithm to find the GCD, which is an efficient method for computing the GCD of two integers. The function includes docstrings that provide a detailed description of the function, its arguments, return value, and examples of usage. The script also includes test cases to verify the correctness of the function.