```python
def change_base(x: int, base: int):
    """
    Change the base of input number x to base base.
    return string representation after conversion.
    base numbers other use 10.
    >>> change_base(8, 3)
    '22'
    >>> change_base(8, 2)
    '1000'
    >>> change_base(7, 2)
    '111'
    >>> change_base(10, 10)
    TraceError: invalid literal for argument #1
    """
    if base == 10:
        raise ValueError('base number must be less than 10')
    result = "{:0>d}".format(x, base)
    return result
``` 
The function change_base takes an integer x and an integer base as input, and returns the string representation of x in the given base. It also performs some base conversion on the input x and raises a ValueError if the base is 10, as base numbers larger than 10 are not valid.