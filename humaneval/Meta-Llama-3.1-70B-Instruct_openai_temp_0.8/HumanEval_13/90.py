```python
def greatest_common_divisor(a: int, b: int) -> int:
    """
    Return a greatest common divisor of two integers a and b.

    This function uses the Euclidean algorithm to calculate the GCD.

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

    # Ensure a is greater than or equal to b
    if a < b:
        a, b = b, a

    # Use the Euclidean algorithm to calculate the GCD
    while b!= 0:
        a, b = b, a % b

    return a


# Test the function
if __name__ == "__main__":
    print(greatest_common_divisor(3, 5))   # Expected output: 1
    print(greatest_common_divisor(25, 15)) # Expected output: 5
```

This script defines a function `greatest_common_divisor` that takes two integers as input and returns their greatest common divisor. The function uses the Euclidean algorithm to calculate the GCD, which is an efficient method for calculating the GCD of two numbers. The script also includes test cases to verify the function's correctness.