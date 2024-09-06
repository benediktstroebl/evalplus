```python
def change_base(x: int, base: int) -> str:
    """
    Change the base of integer x to base base.
    Convert to string representation using specified base.
    """return string representation after conversion.
    """Raise an error if base is not a valid number.
    """
   return "Invalid base value" if base < 0 or base > 36
    """
    if not(base.isinstance() or base >= 0 and base <= 36):
        return f'{x:{base}'
    else:
        return "Invalid base value"
```