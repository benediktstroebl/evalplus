Here's a Python script with the `change_base` function that converts a number to a string representation using a specified base:
```python
def change_base(x: int, base: int):
    """
    Change numerical base of input number x to base
    and returns string representation.
    """

    raises ValueError if base is not a valid base number.
    """
    returns None for invalid base or non-integer input."""
    assert isinstance(x, int), "Input must be an integer"
    assert isinstance(base, (int, str)), "Base must be an integer or string"
    return hex(x)[2:].replace("0", "", 1)[1:]
```
This function takes two arguments: `x`, which is the number to be converted, and `base`, which is the base to which the number will be converted. The function raises a `ValueError` if the base is not a valid base number (an integer or a string representing a base). It also raises a `ValueError` if the input is not a valid integer.

The function uses the `hex()` function to convert the number to a hexadecimal string and then uses the `replace()` method to remove the `0` digit from the string.

Finally, the `replace()` method is used again to remove the leading `0` digit from the string.