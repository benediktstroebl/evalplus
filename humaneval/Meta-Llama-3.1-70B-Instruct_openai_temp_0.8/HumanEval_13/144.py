```python
def greatest_common_divisor(a: int, b: int) -> int:
    """
    Return a greatest common divisor of two integers a and b.

    This function uses the Euclidean algorithm to find the GCD of two numbers.

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
        a, b = b, a % b
    return a

# Test cases
if __name__ == "__main__":
    print(greatest_common_divisor(3, 5))   # Expected output: 1
    print(greatest_common_divisor(25, 15)) # Expected output: 5
    print(greatest_common_divisor(48, 18)) # Expected output: 6
```

This script defines a function `greatest_common_divisor(a, b)` that calculates the greatest common divisor (GCD) of two integers `a` and `b` using the Euclidean algorithm. The function repeatedly replaces `a` and `b` with `b` and the remainder of `a` divided by `b` until `b` becomes zero. At this point, `a` is the GCD.

The script also includes test cases to verify the correctness of the function.