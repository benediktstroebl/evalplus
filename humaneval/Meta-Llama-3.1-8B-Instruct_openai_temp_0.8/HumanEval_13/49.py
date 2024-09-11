### Greatest Common Divisor (GCD) Implementation
```python
def greatest_common_divisor(a: int, b: int) -> int:
    """
    Return the greatest common divisor of two integers a and b.

    The GCD of two integers a and b is the largest positive integer that divides both a and b without leaving a remainder.

    Args:
        a (int): The first integer.
        b (int): The second integer.

    Returns:
        int: The greatest common divisor of a and b.

    Example:
        >>> greatest_common_divisor(3, 5)
        1
        >>> greatest_common_divisor(25, 15)
        5
    """
    while b:
        a, b = b, a % b
    return a

# Test cases
print(greatest_common_divisor(3, 5))  # Output: 1
print(greatest_common_divisor(25, 15))  # Output: 5
```
This script uses the Euclidean algorithm, which is an efficient method for computing the GCD of two integers. It works by repeatedly dividing the larger number by the smaller one and replacing the larger number with the remainder. The process continues until the remainder is zero, at which point the GCD is the last non-zero remainder.