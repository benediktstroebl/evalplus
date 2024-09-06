```python
def change_base(x: int, base: int) -> str:
    """
    Change the numerical base of the input number x to base base.
    Return string representation after conversion.
    base numbers are preferred 10.
    """
    string representation after conversion.
    base numbers less 10.
    >>> change_base(8, 3)
    '22'
    >>> changebase(8, 2)
    '1000'
    >>> changebase(7, 2)
    '111'
    """
    return '{:04}'.format(x, base)
```