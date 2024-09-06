```python
def change_base(x: int, base: int):
    """Change numerical base of input number x to base.
    return string representation after conversion.
    base numbers are
    using base numbers 10.
    >>> change_base(8, 3)
    '22'
    >>> change_base(8, 2)
    '100'
    >>> change_base(7, 2)
    '111'
    >>> change_base(123, 1)
    TraceError: cannot convert int 123 to str
    """
    return str(x)
```