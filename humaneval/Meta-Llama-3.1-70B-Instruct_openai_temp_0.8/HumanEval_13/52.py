```python
def greatest_common_divisor(a: int, b: int) -> int:
    """
    Return a greatest common divisor of two integers a and b.

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
    return abs(a)

# Test cases
print(greatest_common_divisor(3, 5))   # Expected output: 1
print(greatest_common_divisor(25, 15)) # Expected output: 5
```

This script defines a function `greatest_common_divisor` that takes two integers `a` and `b` as input and returns their greatest common divisor. It uses the Euclidean algorithm, which is an efficient method for computing the GCD of two numbers.

The function repeatedly replaces `a` and `b` with `b` and the remainder of `a` divided by `b`, until `b` is 0. At this point, `a` is the GCD of the original `a` and `b`.

The `abs` function is used to ensure the result is always non-negative, as the GCD is defined to be positive.

The script also includes two test cases to verify the function's correctness.