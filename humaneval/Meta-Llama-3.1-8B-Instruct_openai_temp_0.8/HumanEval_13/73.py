```python
def greatest_common_divisor(a: int, b: int) -> int:
    """
    Return a greatest common divisor of two integers a and b

    Args:
    a (int): The first integer
    b (int): The second integer

    Returns:
    int: The greatest common divisor of a and b

    Examples:
    >>> greatest_common_divisor(3, 5)
    1
    >>> greatest_common_divisor(25, 15)
    5
    """
    while b!= 0:
        a, b = b, a % b
    return a

# Testing the function
print(greatest_common_divisor(3, 5))
print(greatest_common_divisor(25, 15))
```

This script uses the Euclidean algorithm to find the greatest common divisor (GCD) of two integers. The algorithm works by repeatedly replacing (a, b) with (b, a mod b) until b is zero. At this point, a is the GCD of the original a and b.