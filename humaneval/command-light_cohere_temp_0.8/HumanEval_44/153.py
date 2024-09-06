```python
def change_base(x: int, base: int) -> str:
    """
    Change the numerical base of the input number x to the base specified.
    Args:
        x: int, the number to be converted
        base: int, the base to convert to
    Returns:
        str: string representation of x after the conversion
    """
    assert isinstance(x, int) and x >= 0, "Invalid input x.
    assert isinstance(base, int) and base >= 1 and base <= 36, "Invalid base value"
    return format(x, int(base))
```