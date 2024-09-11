```python
def greatest_common_divisor(a: int, b: int) -> int:
    """
    Return a greatest common divisor of two integers a and b

    Args:
        a (int): The first integer
        b (int): The second integer

    Returns:
        int: The greatest common divisor of a and b

    Examples:
        >>> greatest_common_divisor(3, 5)
        1
        >>> greatest_common_divisor(25, 15)
        5
    """
    while b:
        a, b = b, a % b
    return abs(a)

# Test cases
print(greatest_common_divisor(3, 5))  # Expected output: 1
print(greatest_common_divisor(25, 15))  # Expected output: 5
```

This script uses the Euclidean algorithm to find the greatest common divisor (GCD) of two input integers. The `while` loop continuously calculates the remainder of the division of `a` by `b`, updating `a` and `b` to `b` and the remainder, respectively. The loop continues until `b` is 0, at which point `a` is the GCD. The function returns the absolute value of `a` to handle negative inputs. The test cases demonstrate the function's usage with comments.