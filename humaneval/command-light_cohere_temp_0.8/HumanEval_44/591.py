```python
def change_base(x: int, base: int):
    """
    Change the numerical base of input number x to base.
    :return string representation after conversion.
    base numbers less 10.
    >>> change_base(8, 3)
    '22'
    >>> change_base(8, 2)
    '1000'
    >>> change_base(7, 2)
    '111'
    >>> change_base(1, 10)
    Traceback (most recent call last):
      File "<stdin>", line 4, in <module>
    ValueError: invalid literal for int() with base 10: '111'
    """
    if base not in [2, 5, 8, 10]:
        raise ValueError("Invalid base number. Base should be 2, 5, 8 or 10.")
    return "{:0>{}d}".format(x, base)
```