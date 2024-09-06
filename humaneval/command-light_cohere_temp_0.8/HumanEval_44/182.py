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
    >>> change_base('12', 10)
    '1200'
    >>> change_base('123', 5)
    '5ugawa'
    >>> change_base('abc123', 2)
    'abc23'
    """
    return f'{x:>{base}a'
```