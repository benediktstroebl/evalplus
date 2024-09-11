```python
def greatest_common_divisor(a: int, b: int) -> int:
    """
    Return a greatest common divisor of two integers a and b.

    This function uses the Euclidean algorithm to find the greatest common divisor.
    The Euclidean algorithm is a way of calculating the greatest common divisor of two numbers,
    based on the principle that the greatest common divisor of two numbers does not change
    if the larger number is replaced by its difference with the smaller number.

    :param a: The first integer.
    :param b: The second integer.
    :return: The greatest common divisor of a and b.

    >>> greatest_common_divisor(3, 5)
    1
    >>> greatest_common_divisor(25, 15)
    5
    """
    while b:
        a, b = b, a % b
    return a

# Test the function
print(greatest_common_divisor(3, 5))  # Expected output: 1
print(greatest_common_divisor(25, 15))  # Expected output: 5
```