```python
def greatest_common_divisor(a: int, b: int) -> int:
    """
    Return a greatest common divisor of two integers a and b

    This function uses the Euclidean algorithm to find the greatest common divisor.

    :param a: The first integer
    :param b: The second integer
    :return: The greatest common divisor of a and b
    """
    while b!= 0:
        a, b = b, a % b
    return abs(a)

# Test cases
print(greatest_common_divisor(3, 5))   # Expected output: 1
print(greatest_common_divisor(25, 15)) # Expected output: 5
print(greatest_common_divisor(-12, 15))# Expected output: 3
print(greatest_common_divisor(0, 5))   # Expected output: 5
```