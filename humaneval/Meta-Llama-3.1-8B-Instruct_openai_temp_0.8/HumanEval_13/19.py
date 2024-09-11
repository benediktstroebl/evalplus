### Greatest Common Divisor (GCD) in Python
```python
def greatest_common_divisor(a: int, b: int) -> int:
    """
    Returns the greatest common divisor of two integers a and b.
    
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
        # Use the Euclidean algorithm to find the GCD
        a, b = b, a % b
    return abs(a)

# Test the function
print(greatest_common_divisor(3, 5))  # Output: 1
print(greatest_common_divisor(25, 15))  # Output: 5
```
This script uses the Euclidean algorithm to find the greatest common divisor of two integers. The `while` loop continues until `b` becomes zero, at which point `a` is the greatest common divisor. The `abs` function is used to return the positive GCD, as the GCD is always non-negative.