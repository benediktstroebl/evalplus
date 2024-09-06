```python
def change_base(x: int, base: int):
    """
    Change the numerical base of input number x to base base.
    Return string representation after conversion.
    base numbers less 10.
    >>> change_base(8, 3)
    '22'
    >>> changebase(8, 2)
    '1000'
    >>> changebase(7, 2)
    '111'
    >>> changebase(10, 10)
    '1'
    >>> changebase(10, 12)
    TraceError: cannot convert int to str
    """
    if base > 2 and base <= 36:
        base = str(base)
    return base.
```