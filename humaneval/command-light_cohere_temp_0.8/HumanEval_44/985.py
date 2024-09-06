```python
def change_base(x: int, base: int) -> str:
    """
    Change the base of a number to another base.
    Args:
        x: int, base of the number to convert
        base: int, base to convert to
    Returns:
        string representation of the number with the new base
    """
    if base < 2 or base > 36:
        raise ValueError("Base must be between 2 and 36")
        
    s = str(x)
    b = int(s[0]) if s[0] == '0' else s[0]
    
    if base == 10:
        return s
    else:
        return s[0:b] + s[1:b] * base
```