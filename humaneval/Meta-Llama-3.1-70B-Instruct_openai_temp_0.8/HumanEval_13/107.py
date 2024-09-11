```python
def greatest_common_divisor(a: int, b: int) -> int:
    """
    Return a greatest common divisor of two integers a and b

    This function uses the Euclidean algorithm to find the greatest common divisor.

    Args:
    a (int): The first integer
    b (int): The second integer

    Returns:
    int: The greatest common divisor of a and b

    >>> greatest_common_divisor(3, 5)
    1
    >>> greatest_common_divisor(25, 15)
    5
    """

    # Ensure a is greater than or equal to b
    if b > a:
        a, b = b, a  # Swap a and b

    while b!= 0:
        # Calculate the remainder of a divided by b
        remainder = a % b
        
        # Update a and b for the next iteration
        a, b = b, remainder

    # At this point, a is the greatest common divisor
    return a


# Test the function
print(greatest_common_divisor(3, 5))   # Expected output: 1
print(greatest_common_divisor(25, 15)) # Expected output: 5
```