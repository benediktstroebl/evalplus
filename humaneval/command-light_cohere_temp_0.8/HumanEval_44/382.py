```python
def change_base(x: int, base: int):
    """
    Change the numerical base of input number x to base base.
    Returns string representation after conversion.
    base numbers 10.
    >>> change_base(8, 3)
    '22'
    >>> change_base(8, 2)
    '1000'
    >>> change_base(7, 2)
    '111'
    >>> change_base(5, 10)
    TraceError: type 'int' not supported for parameter of type 'str'
    """
    # Change the base number
    base = str(base).
    if x >= base:
        return x
    else:
        return str(x)
```