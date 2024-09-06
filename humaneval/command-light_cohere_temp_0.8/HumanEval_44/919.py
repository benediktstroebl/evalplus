```python
def change_base(x: int, base: int):
    """
    Change the numerical base of the input number x to base base.
    Return the string representation of the conversion.
    base numbers 10.
    >>> change_base(8, 3)
    '22'
    >>> change_base(8, 2)
    '1000'
    >>> change_base(7, 2)
    '111'
    >>> change_base(0, 10)
    Traceback (most recent call last):
      File "<stdin>", line 9, in <module>
    File "<stdin>", line 6, in change_base
    File "<stdin>", line 2, in <module>
    File "<stdin>", line 1, in <module>
    ValueError: invalid literal for int() with base 10: '0'
    """
    if x < 0 or base < 2:
        raise ValueError("Input is not a positive number and base is not 2 or 10.")
    result = "{0:{}b}".format(x, base)
    return result
```