```python
def change_base(x: int, base: int) -> str:
    """Change the base representation of a number x to base base.
    :return string representation after conversion.
    base numbers use 10.
    >>> change_base(8, 3)
    '22'
    >>> change_base(8, 2)
    '1000'
    >>> change_base(7, 2)
    '111'
    >>> change_base(0, 5)
    TraceError
    """
    return format(x, f', base={base}')
```