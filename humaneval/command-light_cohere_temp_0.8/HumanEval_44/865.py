```python
def change_base(x: int, base: int):
    """
    Change the numerical base of the input number x to base b.
    Return string representation after conversion.
    base numbers less 10
    a common base.
    >>> change_base(8, 3)
    '22'
    >>> change_base(8, 2)
    '1000'
    >>> change_base(7, 2)
    '111'
    >>> change_base(3, 10)
    '30'
    >>> change_base(10, 2)
    Traceback (most recent call last):
      File "<input>", line 6, in <module>
    ValueError: invalid literal for int() with base 10: '1000'
    """
    return f"{x}"
```