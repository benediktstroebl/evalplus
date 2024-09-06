```python
def change_base(x: int, base: int):
    """
    Change the numerical base of input number x to base B.
    Return the string representation after conversion.
    base numbers are string representation in bases 10.
    >>> change_base(8, 3)
    '22'
    >>> change_base(8, 2)
    '1000'  # Should return '208'
    >>> change_base(7, 2)
    '111'  # Should return '111'
    """
    return '{:04b}'.format(x, base)
```