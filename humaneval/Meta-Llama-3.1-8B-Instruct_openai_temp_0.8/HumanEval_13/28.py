### Greatest Common Divisor (GCD) in Python
```python
def greatest_common_divisor(a: int, b: int) -> int:
    """
    Return the greatest common divisor of two integers a and b.

    This function uses the Euclidean algorithm to find the GCD.

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
    # Ensure a is the larger number
    if b > a:
        a, b = b, a

    # Use the Euclidean algorithm to find the GCD
    while b!= 0:
        a, b = b, a % b

    # Return the GCD
    return a


# Test the function
print(greatest_common_divisor(3, 5))  # Output: 1
print(greatest_common_divisor(25, 15))  # Output: 5
```
This script defines a function `greatest_common_divisor(a: int, b: int) -> int` that calculates the greatest common divisor of two integers `a` and `b` using the Euclidean algorithm. The function first ensures that `a` is the larger number, then iteratively replaces `a` and `b` with `b` and the remainder of `a` divided by `b`, until `b` is zero. At this point, `a` is the greatest common divisor. The function returns the GCD.

The script also includes example use cases and tests the function with the provided examples.