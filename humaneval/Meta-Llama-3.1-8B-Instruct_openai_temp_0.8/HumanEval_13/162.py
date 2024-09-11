```python
def greatest_common_divisor(a: int, b: int) -> int:
    """ Return a greatest common divisor of two integers a and b
    >>> greatest_common_divisor(3, 5)
    1
    >>> greatest_common_divisor(25, 15)
    5
    """
    while b!= 0:
        a, b = b, a % b
    return abs(a)

# Test cases
print(greatest_common_divisor(3, 5))  # Expected output: 1
print(greatest_common_divisor(25, 15))  # Expected output: 5
```

This script uses the Euclidean algorithm to find the greatest common divisor (GCD) of two integers. The Euclidean algorithm is a method for finding the GCD of two numbers by repeatedly replacing `(a, b)` with `(b, a % b)` until `b` is zero. At that point, `a` is the GCD. The `abs` function is used to ensure the GCD is always positive, even if the input numbers are negative.