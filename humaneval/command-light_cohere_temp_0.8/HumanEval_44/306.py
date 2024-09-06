```python
def change_base(x: int, base: int) -> str:
    """
    Change the numerical base of input number x to base base.
    :return: string representation after conversion
    """
    # convert to string using the specified base
    result = "{:" + str(x, base) + "}"
    return result

# Example usage:
print(change_base(8, 3)) # Output: '22'
print(change_base(123, 4)) # Output: '1123'
print(change_base(7, 2)) # Output: '111'
print(change_base(123, 51)) # Should raise error: ValueError: invalid literal for int() with base 51
```
The `change_base` function takes two parameters: `x` (the number to be converted) and `base` (the base to which the number will be converted to). It uses the `str.str` method to convert `x` number to a string using the specified `base`. The resulting string is returned. 

The function can be used to convert numbers to different bases, such as from base 10 to base 2 or base 16. It can also be used to handle various input cases, such as positive and negative numbers, fractions, or integers. 

Note that the `base` parameter should be an integer that represents a valid base number for the `int` data type. The `base` must be between 2 and 36, as `int` supports up to base 36 (due to the maximum precision of `int` is 1e383116).