### Greatest Common Divisor (GCD)
#### Using the Euclidean Algorithm

```python
def greatest_common_divisor(a: int, b: int) -> int:
    """
    Return the greatest common divisor of two integers a and b.

    The Euclidean algorithm is used to find the GCD.

    Parameters:
    a (int): The first integer.
    b (int): The second integer.

    Returns:
    int: The greatest common divisor of a and b.
    """
    while b:
        a, b = b, a % b
    return abs(a)


# Test cases
print(greatest_common_divisor(3, 5))  # Output: 1
print(greatest_common_divisor(25, 15))  # Output: 5
print(greatest_common_divisor(48, 18))  # Output: 6
```

This script defines a function `greatest_common_divisor` that takes two integers `a` and `b` as input and returns their greatest common divisor. The function uses the Euclidean algorithm to find the GCD. The algorithm repeatedly replaces `a` with `b` and `b` with the remainder of `a` divided by `b`, until `b` becomes zero. At that point, `a` is the GCD. The `abs` function is used to ensure the GCD is always non-negative.

The test cases at the end of the script demonstrate the function's usage and verify its correctness.