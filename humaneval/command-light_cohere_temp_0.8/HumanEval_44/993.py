```python
def change_base(x: int, base: int):
    """
    Change the numerical base of input number x to base base.
    return string representation after conversion.
    base numbers less 10.
    >>> change_base(8, 3)
    '22'
    >>> change_base(8, 2)
    '1000'
    >>> change_base(7, 2)
    '111'
    >>> change_base(1, 101)
    Traceback (most recent call last):
      File "<filename>", line 19, in <module>
    AssertionError: (x < 10) 
    """
    if x < 10:
        raise AssertionError("(x < 10)")
    return '{0:0{}b'.format(x, base)
```