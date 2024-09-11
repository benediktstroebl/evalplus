```python
def greatest_common_divisor(a: int, b: int) -> int:
    """
    Return a greatest common divisor of two integers a and b

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
    while b!= 0:
        a, b = b, a % b
    return abs(a)

# Test cases
print(greatest_common_divisor(3, 5))  # Expected output: 1
print(greatest_common_divisor(25, 15))  # Expected output: 5
```

This script defines a function `greatest_common_divisor` that calculates the greatest common divisor (GCD) of two integers using the Euclidean algorithm. The function takes two integers as input, `a` and `b`, and returns their GCD. The `while` loop repeatedly replaces `a` with `b` and `b` with the remainder of `a` divided by `b`, until `b` becomes zero. At that point, `a` is the GCD. The function returns the absolute value of `a` to handle cases where the input integers are negative. The script also includes test cases to demonstrate the function's usage and correctness.