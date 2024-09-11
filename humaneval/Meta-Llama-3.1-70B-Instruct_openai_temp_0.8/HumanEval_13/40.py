```python
def greatest_common_divisor(a: int, b: int) -> int:
    """
    Return a greatest common divisor of two integers a and b.

    This function uses the Euclidean algorithm to find the GCD.
    The Euclidean algorithm is based on the principle that the GCD of two numbers
    does not change if the larger number is replaced by its difference with the smaller number.

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

    # Base case: if b is 0, the GCD is a
    if b == 0:
        return a

    # Recursive case: replace a with b and b with the remainder of a divided by b
    else:
        return greatest_common_divisor(b, a % b)


# Test the function
print(greatest_common_divisor(3, 5))   # Expected output: 1
print(greatest_common_divisor(25, 15)) # Expected output: 5
```