```python
def change_base(x: int, base: int):
    """
    Change the numerical base of input number x to base base.
    Return string representation after conversion.
    base numbers are specific to 10.
    >>> change_base(8, 3)
    '22'
    >>> change_base(8, 2)
    '1000'
    >>> change_base(7, 2)
    '111'
    >>> change_base('12', 5)
    Traceback (most recent call last):
      File "<input>", line 6, in <module>
    ValueError: 'int' object does not support attribute or method '__str__'
    """
    return f'{x}{base}_{base}_{x}'
```