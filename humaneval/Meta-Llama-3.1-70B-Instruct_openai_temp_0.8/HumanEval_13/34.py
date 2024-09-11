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
    while b!= 0:
        a, b = b, a % b
    return abs(a)


# Test the function
if __name__ == "__main__":
    print(greatest_common_divisor(3, 5))   # Expected output: 1
    print(greatest_common_divisor(25, 15)) # Expected output: 5
```

In this script, the `greatest_common_divisor` function takes two integers `a` and `b` as input and returns their greatest common divisor. It uses the Euclidean algorithm to find the greatest common divisor, which is a efficient method for this problem. The `while` loop continues until `b` becomes zero, at which point `a` is the greatest common divisor. The `abs` function is used to ensure the result is always positive. The script also includes test cases to verify the function's correctness.