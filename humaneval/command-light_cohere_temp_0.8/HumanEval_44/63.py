```python
def change_base(x: int, base: int) -> str:
    """
    Change the base of a number x to base base.
    >>> change_base(8, 3) == '22'
    True
    >>> change_base(8, 2) == '1000'
    True
    >>> change_base(7, 2) == '111'
    True
    >>> change_base(7, 5)
    TraceError: unsupported operand type(7) for comparison or arithmetic operation
    """
    return str(x, base)
```