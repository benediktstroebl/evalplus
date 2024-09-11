### Greatest Common Divisor (GCD) Function
```python
def greatest_common_divisor(a: int, b: int) -> int:
    """
    Return the greatest common divisor of two integers a and b.

    The GCD of two integers a and b is the largest positive integer that divides both numbers without leaving a remainder.
    
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

# Test the function
print(greatest_common_divisor(3, 5))  # Output: 1
print(greatest_common_divisor(25, 15))  # Output: 5
print(greatest_common_divisor(48, 18))  # Output: 6
```
This script uses the Euclidean algorithm to calculate the GCD of two integers. The Euclidean algorithm is an efficient method for computing the GCD of two integers, which works by repeatedly replacing 'a' and 'b' with 'b' and 'a % b' (the remainder of 'a' divided by 'b') until 'b' is zero, at which point 'a' is the GCD.