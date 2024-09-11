```python
def greatest_common_divisor(a: int, b: int) -> int:
    """
    Return a greatest common divisor of two integers a and b.

    This function uses the Euclidean algorithm to find the GCD.
    The Euclidean algorithm is a way of calculating the greatest common divisor of two integers,
    based on the principle that the greatest common divisor of two numbers does not change
    if the larger number is replaced by its difference with the smaller number.

    Args:
        a (int): The first integer.
        b (int): The second integer.

    Returns:
        int: The greatest common divisor of a and b.
    """
    while b!= 0:
        # Swap a and b, and replace b with the remainder of a divided by b
        a, b = b, a % b
    return a

# Test cases
print(greatest_common_divisor(3, 5))  # Expected output: 1
print(greatest_common_divisor(25, 15))  # Expected output: 5
print(greatest_common_divisor(48, 18))  # Expected output: 6
```