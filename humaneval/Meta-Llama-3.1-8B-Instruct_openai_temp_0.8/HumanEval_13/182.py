```python
def greatest_common_divisor(a: int, b: int) -> int:
    """
    Return a greatest common divisor of two integers a and b.

    This function uses the Euclidean algorithm to find the GCD.
    The Euclidean algorithm is based on the principle that the greatest common divisor of two numbers does not change if the larger number is replaced by its difference with the smaller number.

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

    # Ensure that a is the larger number
    if b > a:
        a, b = b, a

    # Use a while loop to repeatedly replace 'a' with 'b' and 'b' with the remainder of 'a' divided by 'b'
    # This process continues until 'b' is zero, at which point 'a' is the GCD
    while b!= 0:
        remainder = a % b
        a = b
        b = remainder

    return a

# Test the function
print(greatest_common_divisor(3, 5))  # Output: 1
print(greatest_common_divisor(25, 15))  # Output: 5
```

This script defines a function `greatest_common_divisor` that takes two integers as input and returns their greatest common divisor. The function uses the Euclidean algorithm to calculate the GCD. It also includes docstrings to provide documentation for the function and test cases to verify its correctness.