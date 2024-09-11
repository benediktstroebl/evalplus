```python
def greatest_common_divisor(a: int, b: int) -> int:
    """
    Return a greatest common divisor of two integers a and b.

    The greatest common divisor (GCD) of two non-negative integers a and b
    is the largest number that divides both a and b without leaving a remainder.

    Args:
        a (int): The first integer.
        b (int): The second integer.

    Returns:
        int: The greatest common divisor of a and b.

    >>> greatest_common_divisor(3, 5)
    1
    >>> greatest_common_divisor(25, 15)
    5
    """
    while b!= 0:
        # Swap a and b, and replace b with the remainder of a divided by b
        a, b = b, a % b
    return a

# Test the function
print(greatest_common_divisor(3, 5))  # Expected output: 1
print(greatest_common_divisor(25, 15))  # Expected output: 5
```

This script defines a function `greatest_common_divisor(a, b)` that uses the Euclidean algorithm to find the greatest common divisor of two integers a and b. The function works by repeatedly replacing a with b and b with the remainder of a divided by b until b is 0, at which point a is the greatest common divisor. The test cases at the end of the script demonstrate the function's usage and expected output.