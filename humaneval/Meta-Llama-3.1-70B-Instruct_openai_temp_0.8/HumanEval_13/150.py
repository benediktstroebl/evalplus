```python
def greatest_common_divisor(a: int, b: int) -> int:
    """
    Return a greatest common divisor of two integers a and b.

    This function uses the Euclidean algorithm, which is an efficient method for computing the greatest common divisor of two integers.

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
        # In each iteration, replace 'a' with 'b' and 'b' with the remainder of 'a' divided by 'b'.
        a, b = b, a % b
    return a

# Test the function
print(greatest_common_divisor(3, 5))  # Expected output: 1
print(greatest_common_divisor(25, 15))  # Expected output: 5
```

In this script, the `greatest_common_divisor` function calculates the greatest common divisor of two integers `a` and `b` using the Euclidean algorithm. The function takes two integers as input, and it returns their greatest common divisor. The test cases at the end of the script verify that the function works correctly.