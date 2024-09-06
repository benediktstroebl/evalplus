```python
def change_base(x: int, base: int) -> str:
    """
    Change the numerical base of the input number x to base base.
    Return the string representation after conversion.
    base numbers less 10.
    >>> change_base(8, 3)
    '22'
    >>> change_base(8, 2)
    '1000'
    >>> change_base(7, 2)
    '111'
    >>> change_base(3, 10)
    TraceTypeError: unsupported operand type(3) for unsupported operation '__ abs__'
    """
    return f'{x}'.center(base)
```