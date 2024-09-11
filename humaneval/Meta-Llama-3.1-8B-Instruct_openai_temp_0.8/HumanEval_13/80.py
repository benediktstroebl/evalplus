```python
def greatest_common_divisor(a: int, b: int) -> int:
    """
    Return a greatest common divisor of two integers a and b

    The function uses the Euclidean algorithm to find the GCD of two numbers.
    It repeatedly applies the formula gcd(a, b) = gcd(b, a % b) until b is zero.
    At that point, a is the GCD of the original a and b.

    Args:
        a (int): The first integer.
        b (int): The second integer.

    Returns:
        int: The greatest common divisor of a and b.

    >>> greatest_common_divisor(3, 5)
    1
    >>> greatest_common_divisor(25, 15)
    5
    """
    while b:
        a, b = b, a % b
    return abs(a)

# Example usage:
print(greatest_common_divisor(3, 5))  # Output: 1
print(greatest_common_divisor(25, 15))  # Output: 5
```

This script uses the Euclidean algorithm to find the GCD of two numbers. The algorithm works by repeatedly applying the formula `gcd(a, b) = gcd(b, a % b)` until `b` is zero. At that point, `a` is the GCD of the original `a` and `b`. The `abs` function is used to ensure that the GCD is always non-negative, even if the input numbers are negative.