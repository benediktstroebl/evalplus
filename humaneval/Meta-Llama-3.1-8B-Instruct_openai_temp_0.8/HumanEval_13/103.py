```python
def greatest_common_divisor(a: int, b: int) -> int:
    """ Return a greatest common divisor of two integers a and b

    The function uses the Euclidean algorithm to find the GCD of two numbers.

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

    # Use the Euclidean algorithm to find the GCD
    while b!= 0:
        a, b = b, a % b
    
    # At the end of the loop, 'a' will be the GCD
    return a

# Test the function
print(greatest_common_divisor(3, 5))  # Output: 1
print(greatest_common_divisor(25, 15))  # Output: 5
```

This script defines a function `greatest_common_divisor` that calculates the greatest common divisor (GCD) of two integers using the Euclidean algorithm. The function then tests itself with the provided examples.