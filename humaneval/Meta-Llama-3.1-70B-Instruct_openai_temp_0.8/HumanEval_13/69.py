```python
def greatest_common_divisor(a: int, b: int) -> int:
    """
    Return a greatest common divisor of two integers a and b.

    This function uses the Euclidean algorithm, which is an efficient method for computing the GCD of two numbers.

    :param a: The first integer.
    :param b: The second integer.
    :return: The greatest common divisor of a and b.

    >>> greatest_common_divisor(3, 5)
    1
    >>> greatest_common_divisor(25, 15)
    5
    """

    # Ensure a and b are positive
    a = abs(a)
    b = abs(b)

    # If b is zero, the GCD is a
    while b!= 0:
        # Replace a with b and b with the remainder of a divided by b
        a, b = b, a % b

    return a


# Test the function
if __name__ == "__main__":
    print(greatest_common_divisor(3, 5))  # Expected output: 1
    print(greatest_common_divisor(25, 15))  # Expected output: 5
```