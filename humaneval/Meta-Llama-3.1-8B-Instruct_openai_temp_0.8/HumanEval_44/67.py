```python
def change_base(x: int, base: int):
    """
    Change numerical base of input number x to base.
    Return string representation after the conversion.
    Base numbers are less than 10.

    Args:
        x (int): The number to be converted.
        base (int): The base of the new number representation.

    Returns:
        str: The string representation of x in the new base.

    Examples:
        >>> change_base(8, 3)
        '22'
        >>> change_base(8, 2)
        '1000'
        >>> change_base(7, 2)
        '111'
    """
    if x == 0:
        return '0'
    digits = "0123456789"
    result = ""
    while x:
        result = digits[x % base] + result
        x //= base
    return result

# Test cases
print(change_base(8, 3))  # Output: '22'
print(change_base(8, 2))  # Output: '1000'
print(change_base(7, 2))  # Output: '111'
```

This script uses a while loop to continuously divide the input number by the base until it reaches 0. At each iteration, it appends the remainder of the division (which corresponds to a digit in the new base) to the front of the result string. The reason we append to the front is to ensure that the resulting string is in the correct order (i.e., the most significant digit is on the left). The function returns the result string.