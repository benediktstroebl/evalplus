```python
def greatest_common_divisor(a: int, b: int) -> int:
    """
    Return a greatest common divisor of two integers a and b.

    This function uses the Euclidean algorithm, which is a method for computing the greatest common divisor of two integers.
    The algorithm works by successively applying the division algorithm, swapping the remainder with the divisor, until the remainder is zero.

    :param a: The first integer.
    :param b: The second integer.
    :return: The greatest common divisor of a and b.

    >>> greatest_common_divisor(3, 5)
    1
    >>> greatest_common_divisor(25, 15)
    5
    """

    # Ensure a is the larger number to simplify the algorithm
    if b > a:
        a, b = b, a

    # Repeat the division algorithm until the remainder is zero
    while b!= 0:
        # Calculate the remainder of a divided by b
        remainder = a % b
        
        # Swap the remainder with the divisor
        a = b
        b = remainder

    # The greatest common divisor is the last non-zero remainder
    return a

# Test the function
print(greatest_common_divisor(3, 5))   # Expected output: 1
print(greatest_common_divisor(25, 15)) # Expected output: 5
```