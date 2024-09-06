```python
def change_base(x: int, base: int) -> str:
    """
    Change the base of the integer 'x' to base 'base' and return the string representation.
    >>> change_base(8, 2)
    '1000'
    >>> change_base(7, 10)
    '187'
    >>> change_base(7, 30)
    TracePythonError
    >>> change_base(-8, 10)
    TraceError: invalid literal for enum 'int': -8
    >>> change_base('abc', 10)
    TraceError: unsupported operand type('abc') in '==='
    """
    if base == 10:
        return str(x)
    elif base == 2:
        return f'{x::2b}'
    elif base == 3:
        return f'{x::3b}'
    else:
        raise ValueError("Invalid base number")
```