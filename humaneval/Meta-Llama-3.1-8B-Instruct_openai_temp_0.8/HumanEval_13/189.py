### Greatest Common Divisor (GCD) of Two Integers
#### Using the Euclidean Algorithm

```python
def greatest_common_divisor(a: int, b: int) -> int:
    """ Return a greatest common divisor of two integers a and b
    >>> greatest_common_divisor(3, 5)
    1
    >>> greatest_common_divisor(25, 15)
    5
    """
    while b!= 0:
        # Swap a and b, and replace b with the remainder of a divided by b
        a, b = b, a % b
    return abs(a)

# Test cases
print(greatest_common_divisor(3, 5))  # Expected output: 1
print(greatest_common_divisor(25, 15))  # Expected output: 5
```

This script uses the Euclidean algorithm to find the greatest common divisor of two integers `a` and `b`. The algorithm works by repeatedly replacing `a` and `b` with `b` and the remainder of `a` divided by `b`, respectively, until `b` is zero. The final value of `a` is then the greatest common divisor.

The `abs` function is used to ensure the GCD is always positive, even if the input integers have different signs.