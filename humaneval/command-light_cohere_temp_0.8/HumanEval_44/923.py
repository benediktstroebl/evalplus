```python
def change_base(x: int, base: int):
    """
    Change the numerical base of the input number x to the specified base.
    """
    following the different base numbers: 10, 2, or a user-defined custom base.
    >>> change_base(8, 3)
    '22'
    >>> change_base(8, 2)
    '1000'
    >>> change_base(7, 5) # raises ValueError: unsupported base number 5
    """
    # convert base number to a string to ensure int(base) works
    base = str(base)
    return f'{x : {base}}'  # use string formatting to preserve numerical precision

```