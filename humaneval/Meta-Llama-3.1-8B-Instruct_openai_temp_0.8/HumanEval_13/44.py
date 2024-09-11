```python
def greatest_common_divisor(a: int, b: int) -> int:
    """ Return a greatest common divisor of two integers a and b
    >>> greatest_common_divisor(3, 5)
    1
    >>> greatest_common_divisor(25, 15)
    5
    """
    while b:
        a, b = b, a % b
    return a

# Test the function
print(greatest_common_divisor(3, 5))  # Output: 1
print(greatest_common_divisor(25, 15))  # Output: 5
```

This script uses the Euclidean algorithm, a well-known method for finding the greatest common divisor (GCD) of two integers. The algorithm works by replacing `a` and `b` with `b` and `a % b` in each iteration, until `b` becomes 0. At that point, `a` is the GCD of the original `a` and `b`.