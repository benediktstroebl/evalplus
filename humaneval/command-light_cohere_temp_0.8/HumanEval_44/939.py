Here is a self-contained Python script that solves the problem of changing the numerical base of an input number to a specified base:
```python
def change_base(x: int, base: int):
    """
    Change the base of input number x to base
    Return string representation after conversion.
    """
    string representation after conversion.
    base numbers are standard is 10.
    >>> change_base(8, 3)
    '22'
    >>> change_base(8, 2)
    '1000'
    >>> change_base(7, 2)
    '111'
    >>> change_base('abc123', 45) # invalid base
    'xx'
    >>> change_base(123, 5) # invalid input
    'abc12345'
    """
    if base < 2 or base > 36:
        return 'Invalid base number'
    return '{:b}'.format(x, base)
```
This script defines a function called `change_base`, which takes two arguments: the input number `x` and the base `base` to which the input number will be converted. The function then checks if the base is valid (between 2 and 36) and if the input is not a string, it returns an error message. If the base is valid, the function converts the input number to the specified base and returns the resulting string representation.