```python
def change_base(x: int, base: int):
    """
    Change the numerical base of input number x to base base.
    return string representation after conversion.
    base numbers use 10 ora base numbers.
    >>> change_base(8, 3)
    '22'
    >>> change_base(8, 2)
    '1000'
    >>> change_base(7, 2)
    '111'
    >>> change_base('string', 4)
    Traceback (most recent call last):
      File "<stdin>", line 26, in <module>
    ValueError: 'int' object does not support item assignment (use 'format()')
    """
    return '{:0b}'.format(x, base)
```