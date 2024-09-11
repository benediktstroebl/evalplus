### Greatest Common Divisor (GCD) Function
```python
def greatest_common_divisor(a: int, b: int) -> int:
    """
    Return a greatest common divisor of two integers a and b

    The GCD of two integers is the largest number that divides both of them.

    Args:
        a (int): First integer.
        b (int): Second integer.

    Returns:
        int: GCD of a and b.

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

# Test the function
print(greatest_common_divisor(3, 5))   # Expected output: 1
print(greatest_common_divisor(25, 15)) # Expected output: 5
```
In this code, we use the Euclidean algorithm to find the GCD of two integers. The algorithm works by continuously replacing 'a' with 'b' and 'b' with the remainder of 'a' divided by 'b', until 'b' becomes zero. At that point, 'a' will be the GCD.

Note: The `abs` function is used to handle negative inputs and ensure the GCD is always positive.