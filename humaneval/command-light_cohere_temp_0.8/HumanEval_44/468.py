Here's the Python script with the self-contained function `change_base` that correctly converts a given number `x` to a string using a specified base `base`:
```python
def change_base(x: int, base: int) -> str:
    """
    Change the numerical base of the input number x to base base.
    >>> change_base(8, 3)
    '22'
    >>> change_base(8, 2)
    '1000'
    >>> change_base(7, 2)
    '111'
    >>> change_base(0, -1)
    Traceback (most recent call last):
      File "<stdin>", line 5, in <module>
        File "<ipython-input-file-name>", line 2, in change_base
        ValueError: invalid literal for int() with base 10: '-'
    """
    if base < 2 or base > 36:
        raise ValueError("Invalid base value.

    return '{:d}''.format(x, base)
```

This `change_base` function takes two parameters: `x` which is the number to be converted, and `base` which is the base to which the number will be converted. The function uses the `format` to convert the number to a string and then uses the `format` method to format the string with the specified base.