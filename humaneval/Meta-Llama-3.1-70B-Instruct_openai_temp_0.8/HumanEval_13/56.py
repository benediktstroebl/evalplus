```python
def greatest_common_divisor(a: int, b: int) -> int:
    """
    Return a greatest common divisor of two integers a and b.

    This function uses the Euclidean algorithm, which is a method for computing
    the greatest common divisor of two integers based on the principle that the
    greatest common divisor of two numbers does not change if the larger number
    is replaced by its difference with the smaller number.

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

    # Ensure a is greater than or equal to b to simplify the loop
    if b > a:
        a, b = b, a

    # Continue replacing 'a' with 'b' and 'b' with the remainder of 'a' divided by 'b'
    # until 'b' is zero. At this point, 'a' is the greatest common divisor.
    while b!= 0:
        a, b = b, a % b

    return a

# Test the function
print(greatest_common_divisor(3, 5))  # Expected output: 1
print(greatest_common_divisor(25, 15))  # Expected output: 5
```

This script defines the `greatest_common_divisor` function, which calculates the greatest common divisor of two integers `a` and `b` using the Euclidean algorithm. It includes a docstring that describes the function, its arguments, return value, and provides examples of its usage. Finally, it includes test cases to verify the correctness of the function.