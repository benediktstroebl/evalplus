```python
def change_base(x: int, base: int):
    """
    Change the numerical base of input number x to base base.
    Return string representation after conversion.
    base numbers less 10.
    >>> change_base(8, 3)
    '22'
    >>> change_base(8, 2)
    '1000'
    >>> change_base(7, 2)
    '111'
    >>> change_base(123, 1)
    TraceError: cannot convert int 123 to str
    """
    try:
        return str(x)
    except TypeError:
        raise TypeError("Cannot convert int to string")
```