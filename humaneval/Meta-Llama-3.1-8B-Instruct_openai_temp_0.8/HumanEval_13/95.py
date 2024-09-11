### Greatest Common Divisor (GCD) Calculator
```python
def greatest_common_divisor(a: int, b: int) -> int:
    """
    Return the greatest common divisor of two integers a and b.

    The GCD of two integers is the largest integer that divides both numbers
    without leaving a remainder.

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
    while b!= 0:
        # Swap a and b, and compute the remainder of a divided by b
        a, b = b, a % b
    return abs(a)

# Test the function
print(greatest_common_divisor(3, 5))  # Output: 1
print(greatest_common_divisor(25, 15))  # Output: 5
print(greatest_common_divisor(48, 18))  # Output: 6
```
This script uses the Euclidean algorithm, a simple and efficient method for computing the GCD of two integers. The `while` loop continues until `b` is zero, at which point `a` is the GCD. The `abs` function is used to handle negative inputs.

You can copy and run this script to use the `greatest_common_divisor` function.