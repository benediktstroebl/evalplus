```python
def change_base(x: int, base: int):
    """
    Change numerical base of input number x to base.
    Return string representation after the conversion.
    Base numbers are less than 10.

    Args:
        x (int): The number to convert.
        base (int): The target base.

    Returns:
        str: The string representation of x in base.

    Examples:
        >>> change_base(8, 3)
        '22'
        >>> change_base(8, 2)
        '1000'
        >>> change_base(7, 2)
        '111'
    """
    convertString = "0123456789"
    result = ''

    while x > 0:
        result = convertString[x % base] + result
        x = x // base

    return result


# Test the function
print(change_base(8, 3))  # Should print '22'
print(change_base(8, 2))  # Should print '1000'
print(change_base(7, 2))  # Should print '111'
```
This script defines the `change_base` function that converts a number from base 10 to any base less than 10. It uses a while loop to continuously divide the input number by the target base and append the remainder to the result string. The result string is then returned after the loop finishes. The script also includes test cases at the end to demonstrate how to use the function.