```python
def change_base(x: int, base: int):
    """
    Change the base of the input number x to base base.
    return string representation after the
    conversion.
    base numbers are1 less than 10.
    >>> change_base(8, 3)
    '22'
    >>> change_base(8, 2)
    '1000'
    >>> change_base(7, 2)
    '111'
    >>> change_base(0, 5)
    Traceback (most recent call last):
      File "<stdin>", line 1364, in <module>
    AssertionError: '0' is not a valid integer'
    """
    if isinstance(x, int) and x > 0:
        string = f"{x}({base}')"
        return string
    else:
        raise AssertionError("'x' is not a valid integer.")
```