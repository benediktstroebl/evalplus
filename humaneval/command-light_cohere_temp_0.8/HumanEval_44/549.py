```python
def change_base(x: int, base: int):
    """
    Change the base of the numerical representation of x to base base.
    Return the string representation of the number after the conversion.
    """base numbers are 10.
    >>> change_base(8, 3)
    '22'
    >>> change_base(8, 2)
    '1000'
    >>> change_base(7, 2)
    '111'
    >>> change_base(10, 5)
    Traceback (most recent call last):
      File "<stdin>", line 10, error: 'SyntaxError': (24, 'invalid literal for int()'): '1000'
    """
    return str(x)
```