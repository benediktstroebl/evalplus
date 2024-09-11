```python
def greatest_common_divisor(a: int, b: int) -> int:
    """
    Return a greatest common divisor of two integers a and b.

    This function uses the Euclidean algorithm, which is a method for finding the greatest common divisor of two numbers.

    :param a: The first integer.
    :param b: The second integer.
    :return: The greatest common divisor of a and b.

    >>> greatest_common_divisor(3, 5)
    1
    >>> greatest_common_divisor(25, 15)
    5
    """

    # Ensure a is greater than or equal to b to simplify the loop
    if a < b:
        a, b = b, a

    # Continue looping until b is 0
    while b!= 0:
        # Calculate the remainder of a divided by b
        remainder = a % b
        
        # Update a to be b and b to be the remainder
        a, b = b, remainder

    # At this point, a is the greatest common divisor
    return a


# Test the function
if __name__ == "__main__":
    print(greatest_common_divisor(3, 5))  # Expected output: 1
    print(greatest_common_divisor(25, 15))  # Expected output: 5
```