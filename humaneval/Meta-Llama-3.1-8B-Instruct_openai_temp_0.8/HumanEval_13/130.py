### Greatest Common Divisor (GCD) in Python
```python
def greatest_common_divisor(a: int, b: int) -> int:
    """
    Return the greatest common divisor of two integers a and b.

    The GCD of two integers is the largest positive integer that divides each of the integers without a remainder.

    Parameters:
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
    # Use the Euclidean algorithm to find the GCD
    while b:
        a, b = b, a % b
    return a

# Test the function
print(greatest_common_divisor(3, 5))  # Output: 1
print(greatest_common_divisor(25, 15))  # Output: 5
```
This script uses the Euclidean algorithm to find the greatest common divisor of two integers. The Euclidean algorithm is an efficient method for calculating the GCD of two numbers. It works by repeatedly applying the division algorithm to find the remainder, until the remainder is zero. At that point, the divisor is the GCD.