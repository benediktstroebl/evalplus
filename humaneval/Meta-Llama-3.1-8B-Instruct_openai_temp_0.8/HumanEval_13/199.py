### Greatest Common Divisor (GCD) Calculator
```python
def greatest_common_divisor(a: int, b: int) -> int:
    """
    Return a greatest common divisor of two integers a and b

    This function uses the Euclidean algorithm to find the GCD.

    Args:
        a: An integer
        b: An integer

    Returns:
        An integer representing the greatest common divisor of a and b

    Examples:
        >>> greatest_common_divisor(3, 5)
        1
        >>> greatest_common_divisor(25, 15)
        5
    """
    while b!= 0:
        # Swap a and b, and compute the remainder of a divided by b
        a, b = b, a % b
    return abs(a)  # Return the absolute value in case of negative inputs

# Test the function
print(greatest_common_divisor(3, 5))  # Output: 1
print(greatest_common_divisor(25, 15))  # Output: 5
```
This script uses the Euclidean algorithm to find the GCD of two integers. The Euclidean algorithm is an efficient method for computing the greatest common divisor of two integers. It works by repeatedly replacing "a" and "b" with "b" and "a mod b" until "b" becomes zero. At that point, "a" will be the GCD. The `abs` function is used to return the absolute value of the GCD in case the inputs are negative.