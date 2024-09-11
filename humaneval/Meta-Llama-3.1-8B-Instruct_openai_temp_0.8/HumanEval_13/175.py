```python
def greatest_common_divisor(a: int, b: int) -> int:
    """
    Return a greatest common divisor of two integers a and b

    The function uses the Euclidean algorithm to find the GCD.

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
    return a

# Test cases
print(greatest_common_divisor(3, 5))  # 1
print(greatest_common_divisor(25, 15))  # 5
```

This script defines a function `greatest_common_divisor` that calculates the GCD of two integers `a` and `b` using the Euclidean algorithm. The function iteratively replaces `a` with `b` and `b` with the remainder of `a` divided by `b` until `b` becomes zero. At that point, `a` is the GCD. The function then returns `a`. The test cases at the end demonstrate the function's correctness.