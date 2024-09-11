### Greatest Common Divisor (GCD) Calculation

The following Python script calculates the Greatest Common Divisor (GCD) of two integers using the Euclidean algorithm.

```python
def greatest_common_divisor(a: int, b: int) -> int:
    """
    Return a greatest common divisor of two integers a and b.

    The Euclidean algorithm is used to find the GCD. This algorithm works
    by repeatedly replacing (a, b) with (b, a % b) until b is zero.
    At that point, a is the GCD of the original a and b.

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

# Test the function
print(greatest_common_divisor(3, 5))   # Output: 1
print(greatest_common_divisor(25, 15)) # Output: 5
```

This script uses the Euclidean algorithm, which is a simple and efficient method for calculating the GCD of two integers. The algorithm works by replacing (a, b) with (b, a % b) until b is zero, at which point a is the GCD of the original a and b.