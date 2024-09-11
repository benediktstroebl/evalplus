```python
def greatest_common_divisor(a: int, b: int) -> int:
    """
    Return the greatest common divisor of two integers a and b.

    The greatest common divisor of two integers a and b is the largest positive integer that divides both a and b without leaving a remainder.

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
    return abs(a)


# Test cases
import doctest

doctest.testmod()
```

This script defines a function `greatest_common_divisor` to calculate the greatest common divisor of two integers using the Euclidean algorithm. The `doctest` module is used to run the test cases at the end of the script.

When you run this script, it will execute the test cases and print their results. If all test cases pass, it will not print anything. If any test case fails, it will print an error message indicating which test case failed.