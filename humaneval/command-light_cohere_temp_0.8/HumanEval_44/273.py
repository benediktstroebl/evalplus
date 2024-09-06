```python
def change_base(x: int, base: int) -> str:
    """
    Convert a number to a string using specified base.
    Uses the value of the string representation of the number.
    """
    base numbers use 10.
    """
    string representation is using the specified base.
    """
"""
    return f"{x{base}}"

assert change_base(8, 3) == '22'
assert change_base(7, 10) == '77'
assert change_base(123, 2) == '852'
assert change_base(5, 25) == '15255'
```