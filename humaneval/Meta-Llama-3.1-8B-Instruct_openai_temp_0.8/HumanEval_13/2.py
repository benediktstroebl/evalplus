### Greatest Common Divisor (GCD) Script
```python
def greatest_common_divisor(a: int, b: int) -> int:
    """
    Return a greatest common divisor of two integers a and b.

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
    return abs(a)

# Example usage
print(greatest_common_divisor(3, 5))   # Output: 1
print(greatest_common_divisor(25, 15)) # Output: 5
```
This script uses the Euclidean algorithm to calculate the GCD of two integers. The function `greatest_common_divisor` takes two integers `a` and `b` as input and returns their GCD. The example usage at the end shows how to use this function.