```python
def change_base(x: int, base: int) -> str:
    """
    Change the numerical base of input number x to base base.
    >>> change_base(8, 3) == '22'
    True
    >>> change_base(8, 2) == '1000'
    True
    >>> change_base(7, 2) == '111'
    True
    >>> change_base('12', 0) == ''
    False
    """
    assert x != 0, "Input number cannot be zero"
    return '{:0b}'.format(x, base)
```