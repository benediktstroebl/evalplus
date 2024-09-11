```python
def greatest_common_divisor(a: int, b: int) -> int:
    """
    Returns the greatest common divisor (GCD) of two integers a and b.
    
    The GCD is the largest number that divides both a and b without leaving a remainder.
    
    :param a: The first integer.
    :param b: The second integer.
    :return: The greatest common divisor of a and b.
    """
    while b:
        a, b = b, a % b
    return a

# Test cases
print(greatest_common_divisor(3, 5))  # Expected output: 1
print(greatest_common_divisor(25, 15))  # Expected output: 5
```

This script uses the Euclidean algorithm to calculate the GCD of two numbers. The algorithm works by repeatedly replacing 'a' and 'b' with 'b' and the remainder of 'a' divided by 'b', until 'b' is zero. At this point, 'a' is the GCD of the original 'a' and 'b'.