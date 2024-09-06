```python
def change_base(x: int, base: int):
    """
    Change the numerical base of input number x to base base.
    return string representation after conversion.
    base numbers less 10 or oth, 10, 100. time the base to digits before
    >>> change_base(8, 3)
    '22'
    >>> change_base(5, 1)
    TraceError: unsupported operand type(5)
    """
    return ''.join(str(x)[:: :- base])
```