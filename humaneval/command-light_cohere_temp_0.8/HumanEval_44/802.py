```python
def change_base(x: int, base: int):
    """
    Change the numerical base of input number x to base base.
    Returns string representation after conversion.
    base numbers are
    larger than 10, as does the base used in this function.
    >>> change_base(8, 3)
    '22'
    >>> change_base(8, 2)
    '1000'
    >>> change_base(7, 2)
    '111'
    >>> change_base('123', 'A')
    Traceback (most recent call last):
      File "<stdin>", line 29, error=SyntaxError)
    ^NIAContentError: invalid literal for int() with base 'A'
    """
    return '{:02}'.format(x).format(x, base)
```