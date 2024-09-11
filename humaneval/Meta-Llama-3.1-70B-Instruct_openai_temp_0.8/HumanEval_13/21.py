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
    while b!= 0:
        # In each iteration, we replace 'a' with 'b' and 'b' with the remainder of 'a' divided by 'b'
        a, b = b, a % b

    return abs(a)

# Test cases
print(greatest_common_divisor(3, 5))  # Expected output: 1
print(greatest_common_divisor(25, 15))  # Expected output: 5
```

This script defines a function `greatest_common_divisor(a, b)` that calculates the greatest common divisor (GCD) of two integers `a` and `b`. The function uses the Euclidean algorithm, which is an efficient method for calculating the GCD. The algorithm repeatedly replaces `a` with `b` and `b` with the remainder of `a` divided by `b` until `b` is 0. At this point, `a` is the GCD. The function returns the absolute value of `a` to ensure the result is always non-negative.

The script also includes test cases to verify the correctness of the `greatest_common_divisor` function.