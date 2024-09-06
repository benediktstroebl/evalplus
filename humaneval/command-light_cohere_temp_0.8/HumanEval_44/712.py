```python
def change_base(x: int, base: int) -> str:
    """
    Change the numerical base of the input number x to the specified base.
    >>> change_base(8, 3) == '22'
    True
    >>> change_base(8, 2) == '1000'
    True
    >>> change_base(7, 2) == '111'
    True
    >>> change_base(5, 1)
    Traceback (most recent call last):
    TypeError: 'int' object does not support item assignment
    """
    if base < 2 or base > 36:
        raise ValueError("Invalid base value.
    return '{:02x'.format(x, base))
```