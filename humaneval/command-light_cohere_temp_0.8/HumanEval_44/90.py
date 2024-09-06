```python
def change_base(x: int, base: int):
    """
    Change the numerical base of input number x to base B.
    Return string representation after conversion.
    base numbers less 10.
    >>> change_base(8, 3)
    '22'
    >>> change_base(8, 2)
    '1000'
    >>> change_base(7, 2)
    '111'
    """
    if base == 10:
        return str(x)
    elif x < 0:
        return ''  # base handling
    else:
        return '{:b}'.format(x, format_spec=f"{base}base")
```