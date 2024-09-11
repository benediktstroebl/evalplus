### Greatest Common Divisor (GCD) Script

```python
def greatest_common_divisor(a: int, b: int) -> int:
    """
    Return a greatest common divisor of two integers a and b

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
    while b:
        a, b = b, a % b
    return abs(a)


# Test cases
import doctest

doctest.testmod()
```

In this script, we have implemented the Euclidean algorithm to find the GCD of two integers. The `while` loop continues until `b` becomes zero. In each iteration, we update `a` and `b` as follows: `a` becomes the previous value of `b` and `b` becomes the remainder of the division of `a` by `b`. The GCD is then the absolute value of the last non-zero remainder.

The doctest module is used to test the function with the provided example cases. The `testmod()` function is used to automatically run the tests.