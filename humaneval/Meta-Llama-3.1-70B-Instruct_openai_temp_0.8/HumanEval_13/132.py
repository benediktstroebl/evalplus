```python
def greatest_common_divisor(a: int, b: int) -> int:
    """
    Return a greatest common divisor of two integers a and b.

    This function uses the Euclidean algorithm to calculate the GCD.

    >>> greatest_common_divisor(3, 5)
    1
    >>> greatest_common_divisor(25, 15)
    5
    """
    while b!= 0:
        a, b = b, a % b
    return abs(a)

# Example usage
print(greatest_common_divisor(3, 5))   # Output: 1
print(greatest_common_divisor(25, 15)) # Output: 5
```
This script defines a function `greatest_common_divisor` that takes two integers `a` and `b` as input and returns their greatest common divisor (GCD). The function uses the Euclidean algorithm, which is a simple and efficient method for calculating the GCD of two numbers. The algorithm works by repeatedly replacing `a` with `b` and `b` with the remainder of `a` divided by `b`, until `b` is zero. At this point, `a` is the GCD of the original `a` and `b`. The `abs` function is used to ensure the result is always non-negative.