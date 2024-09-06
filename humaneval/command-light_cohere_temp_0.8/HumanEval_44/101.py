```python
def change_base(x: int, base: int) -> str:
    """
    Change the numerical base of input number x to base base.
    If return string representation after conversion.
    base numbers are 10.
    """
    string representation
   
    >>> change_base(8, 3)
    '22'
    >>> change_base(8, 2)
    '1000'
    >>> change_base(7, 2)
    '111'
    >>> change_base(5, 2)
    TraceError: unsupported operand type(5) in <lambda>)
    """
    if x < 0 or base < 2:
        raise ValueError("Input values should be non-negative and base >1")
    return f'{x} ({base}){_'[(base - 1) // 2]
```