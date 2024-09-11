```python
def greatest_common_divisor(a: int, b: int) -> int:
    """
    Return a greatest common divisor of two integers a and b

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

# Test cases
print(greatest_common_divisor(3, 5))  # Expected output: 1
print(greatest_common_divisor(25, 15))  # Expected output: 5
```

This script defines the `greatest_common_divisor` function, which takes two integers as input and returns their greatest common divisor. The function uses the Euclidean algorithm, which repeatedly applies the division algorithm to find the GCD. The `while` loop continues until `b` is 0, at which point `a` is the GCD. The `abs` function is used to ensure that the GCD is always positive, even if the input integers are negative. The script also includes two test cases to verify that the function is working correctly.