```python
def greatest_common_divisor(a: int, b: int) -> int:
    """
    Return a greatest common divisor of two integers a and b.

    This function uses the Euclidean algorithm to find the greatest common divisor.

    >>> greatest_common_divisor(3, 5)
    1
    >>> greatest_common_divisor(25, 15)
    5
    """

    # Ensure a is the larger number to simplify the algorithm
    if b > a:
        a, b = b, a

    # Continue to divide a by b and replace a with b and b with the remainder
    # until b is 0. At this point, a is the greatest common divisor.
    while b!= 0:
        a, b = b, a % b

    return a


# Test the function
print(greatest_common_divisor(3, 5))  # Expected output: 1
print(greatest_common_divisor(25, 15))  # Expected output: 5
```