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
    while b:
        a, b = b, a % b
    return a

# Example usage:
print(greatest_common_divisor(3, 5))  # Output: 1
print(greatest_common_divisor(25, 15))  # Output: 5
```

In this script, we use the Euclidean algorithm, which is a method for finding the greatest common divisor of two numbers. The algorithm works by repeatedly replacing `a` and `b` with `b` and `a % b`, respectively, until `b` is zero. At that point, `a` is the greatest common divisor of the original `a` and `b`.