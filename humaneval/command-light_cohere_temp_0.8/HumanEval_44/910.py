```python
def change_base(x: int, base: int):
    """
    Convert a number to a string representation using specified base.
    Args:
        x: int, number to be converted
        base: int, desired base for conversion
    Returns:
        str: string representation of x
    """
    if base > 36:
        raise ValueError("Base must be between 2 and 36")
    return format(x, base)

x = 8
y = 3
z = 10
test_change_base = change_base(x, y)
assert test_change_base == '22'
test_change_base = change_base(z, 2)
assert test_change_base == '1000'
test_change_base = change_base(7, 2)
assert test_change_base == '111'
 ``` 
This script defines a function `change_base` that converts a number to a string representation with a specified base. It raises a specified `ValueError` if the base is larger than 36. The code then tests the function using different inputs and asserts that the output is correct.