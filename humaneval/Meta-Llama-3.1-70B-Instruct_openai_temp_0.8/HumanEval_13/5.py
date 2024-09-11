```python
def greatest_common_divisor(a: int, b: int) -> int:
    """
    Return a greatest common divisor of two integers a and b.

    This function uses the Euclidean algorithm to find the GCD of two numbers.

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
    # Ensure a is the larger number to simplify the algorithm
    if a < b:
        a, b = b, a

    # Use the Euclidean algorithm to find the GCD
    while b!= 0:
        # Replace a with b and b with the remainder of a divided by b
        a, b = b, a % b

    # Once b is 0, a is the GCD
    return a


# Test the function
print(greatest_common_divisor(3, 5))  # Expected output: 1
print(greatest_common_divisor(25, 15))  # Expected output: 5
```

This script defines the `greatest_common_divisor` function, which takes two integers as input and returns their greatest common divisor. The function uses the Euclidean algorithm to efficiently find the GCD. The script also includes example use cases and test cases to demonstrate the function's correctness.