```python
def change_base(x: int, base: int) -> str:
    """
    Change the numerical base of input number x to base base.
    Return string representation after conversion.
    base numbers less 10.
    >>> change_base(8, 3)
    '22'
    >>> changebase(8, 2)
    '1000'
    >>> changebase(7, 2)
    '111'
    >>> changebase(10, 3)
    '58'
    >>> changebase(1, 123456789)
    Traceback (most recent call last):
      File "<stdin>", line 13, in <module>
    TypeError: unsupported operand type(bool, int)
    """
    if isinstance(x, bool):
        raise TypeError("unsupported operand type (bool, int)")
    return "{:0{}b}".format(x, base)
```