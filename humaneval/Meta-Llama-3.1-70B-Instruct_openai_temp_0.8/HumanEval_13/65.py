```python
def greatest_common_divisor(a: int, b: int) -> int:
    """
    Return a greatest common divisor of two integers a and b.

    This function uses the Euclidean algorithm, which is a method for computing the greatest common divisor of two numbers.

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

    # Ensure that a is the larger number to simplify the algorithm
    if b > a:
        a, b = b, a

    # Continue to divide the larger number by the smaller number until the remainder is 0
    while b!= 0:
        # Replace the larger number with the smaller number and the smaller number with the remainder
        a, b = b, a % b

    # At this point, a is the greatest common divisor
    return a


# Test the function
if __name__ == "__main__":
    print(greatest_common_divisor(3, 5))  # Output: 1
    print(greatest_common_divisor(25, 15))  # Output: 5
```