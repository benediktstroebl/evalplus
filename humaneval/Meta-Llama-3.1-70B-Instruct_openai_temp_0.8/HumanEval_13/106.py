```python
def greatest_common_divisor(a: int, b: int) -> int:
    """
    Return a greatest common divisor of two integers a and b.

    This function uses the Euclidean algorithm to find the GCD.

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
        a, b = b, a % b
    return abs(a)

# Test the function
print(greatest_common_divisor(3, 5))  # Expected output: 1
print(greatest_common_divisor(25, 15))  # Expected output: 5
```

In this script, the `greatest_common_divisor` function takes two integers `a` and `b` as input and returns their greatest common divisor. The function uses the Euclidean algorithm to find the GCD, which is based on the principle that the greatest common divisor of two numbers `a` and `b` is equal to the greatest common divisor of `b` and the remainder of `a` divided by `b`. This process is repeated until `b` is zero, at which point `a` is the GCD.

The script also includes test cases to verify the correctness of the function.