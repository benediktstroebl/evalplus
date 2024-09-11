## Greatest Common Divisor (GCD) Calculation
The following Python script calculates the greatest common divisor (GCD) of two integers using the Euclidean algorithm.

```python
def greatest_common_divisor(a: int, b: int) -> int:
    """
    Return the greatest common divisor of two integers a and b.

    The Euclidean algorithm is used to find the GCD.

    Args:
        a (int): The first integer.
        b (int): The second integer.

    Returns:
        int: The greatest common divisor of a and b.

    Example:
        >>> greatest_common_divisor(3, 5)
        1
        >>> greatest_common_divisor(25, 15)
        5
    """
    while b:
        a, b = b, a % b
    return abs(a)


# Test cases
if __name__ == "__main__":
    print(greatest_common_divisor(3, 5))  # Expected output: 1
    print(greatest_common_divisor(25, 15))  # Expected output: 5
    print(greatest_common_divisor(48, 18))  # Expected output: 6
```

This script uses the Euclidean algorithm to find the GCD of two integers. It repeatedly replaces `a` and `b` with `b` and the remainder of `a` divided by `b`, until `b` becomes zero. At that point, `a` is the GCD. The `abs` function is used to handle the case where `a` is negative.