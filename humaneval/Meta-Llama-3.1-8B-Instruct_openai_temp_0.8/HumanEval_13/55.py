```python
def greatest_common_divisor(a: int, b: int) -> int:
    """
    Return a greatest common divisor of two integers a and b

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

# Test cases
print(greatest_common_divisor(3, 5))  # 1
print(greatest_common_divisor(25, 15))  # 5
```

This script defines the `greatest_common_divisor` function using the Euclidean algorithm, which is a simple and efficient method for calculating the greatest common divisor (GCD) of two numbers. The function takes two integers `a` and `b` as input and returns their GCD.

The test cases at the end of the script demonstrate the function's usage and verify its correctness.