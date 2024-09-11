```python
def greatest_common_divisor(a: int, b: int) -> int:
    """
    Return a greatest common divisor of two integers a and b

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

    # Ensure a and b are positive
    a = abs(a)
    b = abs(b)

    # If b is zero, the greatest common divisor is a
    if b == 0:
        return a
    else:
        # Otherwise, recursively call the function with b and the remainder of a divided by b
        return greatest_common_divisor(b, a % b)


# Test the function
print(greatest_common_divisor(3, 5))  # Output: 1
print(greatest_common_divisor(25, 15))  # Output: 5
```

This script defines a recursive function `greatest_common_divisor` that uses the Euclidean algorithm to find the greatest common divisor of two integers. The function takes two integers `a` and `b` as input and returns their greatest common divisor.

The function first ensures that `a` and `b` are positive by taking their absolute values. It then checks if `b` is zero, in which case the greatest common divisor is `a`. Otherwise, it recursively calls the function with `b` and the remainder of `a` divided by `b`.

The script also includes test cases to verify the correctness of the function.