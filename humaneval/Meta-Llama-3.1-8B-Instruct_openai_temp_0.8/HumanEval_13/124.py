### Greatest Common Divisor (GCD) Function
#### Using Euclid's Algorithm

```python
def greatest_common_divisor(a: int, b: int) -> int:
    """
    Return the greatest common divisor of two integers a and b.

    The function uses Euclid's algorithm to find the GCD.

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

    # Ensure a and b are integers
    a = int(a)
    b = int(b)

    # If b is zero, the GCD is a
    if b == 0:
        return a
    # Otherwise, the GCD is the same as the GCD of b and the remainder of a divided by b
    else:
        return greatest_common_divisor(b, a % b)

# Example usage:
print(greatest_common_divisor(3, 5))  # Output: 1
print(greatest_common_divisor(25, 15))  # Output: 5
```

This script defines a function `greatest_common_divisor` that uses Euclid's algorithm to find the greatest common divisor of two integers. The function works by recursively replacing the larger number with its remainder when divided by the smaller number, until the smaller number becomes zero. At that point, the larger number is the GCD.