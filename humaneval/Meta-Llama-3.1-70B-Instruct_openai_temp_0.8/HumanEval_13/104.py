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
    while b!= 0:
        # Swap the values of a and b, and replace b with the remainder of a divided by b
        a, b = b, a % b
    return a

# Test the function
print(greatest_common_divisor(3, 5))   # Expected output: 1
print(greatest_common_divisor(25, 15)) # Expected output: 5
```

This Python script defines a function called `greatest_common_divisor` that takes two integers `a` and `b` as arguments and returns their greatest common divisor. The function uses the Euclidean algorithm to find the greatest common divisor. The script also includes examples and test cases to demonstrate the function's usage.