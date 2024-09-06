```python
def change_base(x: int, base: int) -> str:
    """
    Change the numerical base of the input number to the desired base.
    Parameters:
    x: int,  base: int
    Returns:  str, the base-converted string representation.
    """
    convert a x to a string representation using the specified base.
    """
    return the string representation after applying the appropriate conversion
    """
    if not isinstance(x, str):
        raise TypeError("Input 'x' must be a string.")
    return str(x, base)
```