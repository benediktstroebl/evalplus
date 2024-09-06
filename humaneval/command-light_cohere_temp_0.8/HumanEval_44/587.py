```python
def change_base(x: int, base: int) -> str:
    """
    Change the numerical base of the input number to the specified base.
    Args:
        x: int, Input number
        base: int, Conversion base
    Returns: 
        string, string representation of number
    """
    assert isinstance(x, int), f"Input must be integer: {x} of type {type(x)}"
    assert isinstance(base, int), f"Base must be integer: {base} of type {type(base)}"
    if x < 0:
        raise ValueError("Negative numbers are not supported")
    return format(x, base)
```