```python
def greatest_common_divisor(a: int, b: int) -> int:
    """
    Return a greatest common divisor of two integers a and b.

    This function uses the Euclidean algorithm, which is an efficient method 
    for computing the greatest common divisor of two numbers.

    Args:
        a (int): The first number.
        b (int): The second number.

    Returns:
        int: The greatest common divisor of a and b.

    Examples:
        >>> greatest_common_divisor(3, 5)
        1
        >>> greatest_common_divisor(25, 15)
        5
    """

    # Ensure a and b are positive integers
    a = abs(a)
    b = abs(b)

    # If b is zero, the greatest common divisor is a
    while b:
        # Replace a with b and b with the remainder of a divided by b
        a, b = b, a % b

    return a

# Test the function
print(greatest_common_divisor(3, 5))   # Output: 1
print(greatest_common_divisor(25, 15)) # Output: 5
```