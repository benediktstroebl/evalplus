```python
def change_base(x: int, base: int):
    """
    Change the numerical base of the input number x to the specified base.
    Return the string representation in the desired base.
    >>> change_base(8, 3)
    '22'
    >>> change_base(8, 2)
    '1000'
    >>> change_base(7, 2)
    '111'
    >>> change_base(0, 4)
    Tracebacks...
    ...
    ValueError: invalid literal for int() with base 4: '111'
    """
    # convert string to integer
    x = int(x, base)
    return x
```