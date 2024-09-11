```python
def greatest_common_divisor(a: int, b: int) -> int:
    """
    Return a greatest common divisor of two integers a and b.

    This function uses the Euclidean algorithm to find the greatest common divisor.
    The Euclidean algorithm is based on the principle that the greatest common divisor
    of two numbers does not change if the larger number is replaced by its difference
    with the smaller number.

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

    # Ensure a is the larger number
    if b > a:
        a, b = b, a

    # If b is zero, the greatest common divisor is a
    while b!= 0:
        # Replace a with b and b with the remainder of a divided by b
        a, b = b, a % b

    return a

# Test cases
print(greatest_common_divisor(3, 5))  # Expected output: 1
print(greatest_common_divisor(25, 15))  # Expected output: 5
```

This script defines a function `greatest_common_divisor` that calculates the greatest common divisor of two integers using the Euclidean algorithm. The function takes two integers `a` and `b` as input and returns their greatest common divisor. The script also includes test cases to verify the correctness of the function.