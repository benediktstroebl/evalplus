### Greatest Common Divisor (GCD) Calculator
#### Using Euclid's Algorithm

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

# Test the function
print(greatest_common_divisor(3, 5))  # Output: 1
print(greatest_common_divisor(25, 15))  # Output: 5
```

This script uses Euclid's algorithm to calculate the greatest common divisor (GCD) of two integers. The algorithm repeats the following steps until b becomes zero: 

- Swap a and b
- Replace b with the remainder of a divided by b.

Finally, it returns the absolute value of a, which is the GCD of the original a and b.