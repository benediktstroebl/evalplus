```python
def greatest_common_divisor(a: int, b: int) -> int:
    """
    Return a greatest common divisor of two integers a and b.

    This function uses the Euclidean algorithm to find the greatest common divisor.

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
print(greatest_common_divisor(48, 18)) # Expected output: 6
```

This script defines a function `greatest_common_divisor` that calculates the greatest common divisor of two integers `a` and `b` using the Euclidean algorithm. The function repeatedly replaces `a` with `b` and `b` with the remainder of `a` divided by `b` until `b` is zero, at which point `a` is the greatest common divisor. The function returns the absolute value of `a` to ensure the result is always positive.

The script also includes test cases to verify the function's correctness.