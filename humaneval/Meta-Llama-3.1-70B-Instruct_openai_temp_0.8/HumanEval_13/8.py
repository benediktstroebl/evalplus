```python
def greatest_common_divisor(a: int, b: int) -> int:
    """
    Return a greatest common divisor of two integers a and b

    This function uses the Euclidean algorithm to calculate the GCD.

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
    while b!= 0:
        # Swap the values of a and b
        a, b = b, a % b
    return abs(a)

# Test the function
print(greatest_common_divisor(3, 5))  # Expected output: 1
print(greatest_common_divisor(25, 15))  # Expected output: 5
```

In this script, the `greatest_common_divisor` function takes two integers `a` and `b` as input, and returns their greatest common divisor. The function uses the Euclidean algorithm to calculate the GCD, which is a method for calculating the GCD of two numbers based on the principle that the greatest common divisor of two numbers does not change if the larger number is replaced by its difference with the smaller number.

The `while` loop in the function continues until `b` is zero. At each iteration, `a` and `b` are swapped, and `b` is replaced by the remainder of `a` divided by `b` (`a % b`). When `b` is zero, `a` is the GCD of the original `a` and `b`.

The `abs` function is used to ensure that the GCD is always returned as a positive number, regardless of the signs of the input integers.