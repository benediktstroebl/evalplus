```python
def greatest_common_divisor(a: int, b: int) -> int:
    """
    Return the greatest common divisor of two integers a and b

    Args:
        a (int): The first integer
        b (int): The second integer

    Returns:
        int: The greatest common divisor of a and b
    """
    while b:
        a, b = b, a % b
    return abs(a)

# Test the function
import doctest
doctest.testmod()
```

This script defines a function `greatest_common_divisor` that uses the Euclidean algorithm to find the greatest common divisor of two integers `a` and `b`. The `doctest.testmod()` function is used to test the function with the provided test cases. The `abs(a)` function is used to handle the case where `a` is negative.