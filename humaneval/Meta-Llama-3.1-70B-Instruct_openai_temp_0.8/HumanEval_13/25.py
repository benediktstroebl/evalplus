```python
def greatest_common_divisor(a: int, b: int) -> int:
    """
    Return a greatest common divisor of two integers a and b

    This function uses the Euclidean algorithm to find the GCD.

    >>> greatest_common_divisor(3, 5)
    1
    >>> greatest_common_divisor(25, 15)
    5
    """
    while b!= 0:
        # Swap a and b, and replace b with the remainder of a divided by b
        a, b = b, a % b
    return abs(a)

# Example usage:
print(greatest_common_divisor(3, 5))  # Output: 1
print(greatest_common_divisor(25, 15))  # Output: 5
```

This script defines a function `greatest_common_divisor` that takes two integers `a` and `b` as input and returns their greatest common divisor. It uses the Euclidean algorithm, which is an efficient method for computing the GCD of two numbers. The algorithm works by repeatedly dividing the larger number by the smaller one, replacing the larger number with the smaller one and the smaller number with the remainder of the division, until the remainder is zero. At this point, the non-zero number is the GCD.

Note that the function returns the absolute value of the GCD, to ensure that it is always positive.