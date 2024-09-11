```python
def greatest_common_divisor(a: int, b: int) -> int:
    """
    Return a greatest common divisor of two integers a and b

    The greatest common divisor of two integers a and b is the largest integer that divides both a and b without leaving a remainder.
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
    return a

# Test the function
print(greatest_common_divisor(3, 5))  # Output: 1
print(greatest_common_divisor(25, 15))  # Output: 5
```

This Python script defines a function `greatest_common_divisor` to calculate the greatest common divisor (GCD) of two integers using the Euclidean algorithm. The GCD is the largest integer that divides both numbers without leaving a remainder. The function takes two integers as input and returns their GCD. It includes example use cases and test cases to demonstrate its correctness.