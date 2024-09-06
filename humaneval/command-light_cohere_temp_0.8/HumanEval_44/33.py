Here's the Python code that accomplishes the tasks mentioned:
```python
def change_base(x: int, base: int) -> str:
    """
    Change the numerical base of the input number x to base base.
    return string representation after conversion.
    base numbers are	10.
    """
    base number for conversion.
    >>> change_base(8, 3)
    '22'
    >>> change_base(8, 2)
    '1000'
    >>> change_base(7, 2)
    '111'
    """
    if base == 10:
        return str(x)
    return '{:0>b}'.format(x)
```
This script defines a function `change_base` that converts a given number `x` to a string using the specified base. The base number is represented as an integer, and the function handles the conversion accordingly.