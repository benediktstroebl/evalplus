```python
def greatest_common_divisor(a: int, b: int) -> int:
    """
    Return a greatest common divisor of two integers a and b

    This function uses the Euclidean algorithm to find the greatest common divisor.
    The Euclidean algorithm is an efficient method for computing the greatest common divisor of two integers.

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

    # Continue to divide the larger number by the smaller number until the remainder is 0
    while b!= 0:
        # Store the remainder of a divided by b in a temporary variable
        temp = b
        # Update b to be the remainder of a divided by b
        b = a % b
        # Update a to be the old value of b
        a = temp

    # Once b is 0, a is the greatest common divisor
    return a

# Test the function
print(greatest_common_divisor(3, 5))  # Expected output: 1
print(greatest_common_divisor(25, 15))  # Expected output: 5
```