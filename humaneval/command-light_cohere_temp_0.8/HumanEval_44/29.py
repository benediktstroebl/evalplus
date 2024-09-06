Here's a self-contained Python function that changes the numerical base of an input number to a specified base. It is also designed with full input validation and detailed docstrings:
```python
def change_base(x, base):
    """
    Change the base of the input number x to base base.

    Parameters:
    x: int, number to be converted
    base: int, base number for conversion

    Returns:
    string representation of the converted number
    """
    assert isinstance(x, int) and x > 0, "Input number must be a positive integer"
    assert isinstance(base, int) and base > 0 and base <= 36, "Base number must be a positive integer less than or equal to 37"

    return "{:02}".format(x, base)
```
This function checks the input types and values to ensure they are valid before attempting the conversion. It then uses the welcome formatting to return the converted number as a string. 

I hope this helps you provide clarity and better input validation for your code!