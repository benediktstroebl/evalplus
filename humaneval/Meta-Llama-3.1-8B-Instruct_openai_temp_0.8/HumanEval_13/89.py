```python
def greatest_common_divisor(a: int, b: int) -> int:
    """
    Return a greatest common divisor of two integers a and b

    The greatest common divisor (GCD) of two integers is the largest integer that divides both numbers without leaving a remainder.

    Args:
    a (int): The first integer
    b (int): The second integer

    Returns:
    int: The greatest common divisor of a and b

    Example:
    >>> greatest_common_divisor(3, 5)
    1
    >>> greatest_common_divisor(25, 15)
    5
    """

    # Use the Euclidean algorithm to find the GCD
    while b:
        a, b = b, a % b

    # At this point, a is the GCD
    return a

# Test the function
print(greatest_common_divisor(3, 5))  # Output: 1
print(greatest_common_divisor(25, 15))  # Output: 5
```

This script defines a function `greatest_common_divisor` that takes two integers as input and returns their greatest common divisor using the Euclidean algorithm. The function is then tested with two examples.