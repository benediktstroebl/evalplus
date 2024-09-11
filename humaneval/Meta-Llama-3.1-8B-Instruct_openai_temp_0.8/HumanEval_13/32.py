### Greatest Common Divisor (GCD) using Euclid's Algorithm
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
    while b!= 0:
        # Replace 'a' with 'b' and 'b' with the remainder of 'a' divided by 'b'
        a, b = b, a % b
    return abs(a)

# Test cases
print(greatest_common_divisor(3, 5))  # Output: 1
print(greatest_common_divisor(25, 15))  # Output: 5
```
This implementation uses Euclid's algorithm, which is an efficient method for computing the GCD of two integers. The basic idea is to replace 'a' and 'b' with 'b' and the remainder of 'a' divided by 'b' until 'b' is zero, at which point 'a' will be the GCD. The `abs` function is used to ensure the GCD is always non-negative.