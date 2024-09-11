```python
def greatest_common_divisor(a: int, b: int) -> int:
    """
    Return a greatest common divisor of two integers a and b.

    This function uses the Euclidean algorithm, which is an efficient method for computing the greatest common divisor of two integers.

    :param a: The first integer.
    :param b: The second integer.
    :return: The greatest common divisor of a and b.
    """
    while b:
        a, b = b, a % b
    return a

# Example usage:
print(greatest_common_divisor(3, 5))   # Output: 1
print(greatest_common_divisor(25, 15)) # Output: 5
print(greatest_common_divisor(48, 18)) # Output: 6
```

This script defines a function `greatest_common_divisor` that takes two integers `a` and `b` as input and returns their greatest common divisor. The function uses the Euclidean algorithm, which repeatedly applies the division algorithm to find the remainder of `a` divided by `b`, then replaces `a` with `b` and `b` with the remainder. The algorithm continues until `b` is zero, at which point `a` is the greatest common divisor. The script also includes example usage of the function.