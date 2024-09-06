```python
def change_base(x: int, base: int) -> str:
    """
    Change the base of input number x to base base.
    Returns string representation after conversion.
    base numbers are integer bases are 10.
    >>> change_base(8, 3)
    '22'
    >>> change_base(8, 2)
    '1000'
    >>> change_base(7, 2)
    '111'
    >>> change_base(10, 3)
    '300'
    >>> change_base(10, 5)
    ' cant print'
    """
    return f"{x:>{base}".format(x)
```