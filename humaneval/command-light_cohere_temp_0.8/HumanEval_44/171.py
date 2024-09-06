```python
def change_base(x: int, base: int) -> str:
    """
    Change the base of the integer x to base base.
    Return string representation of x in base base.
    """
    requires integer x and base >= 2.
    """Example bases: 10, 2, 3, 8
    """
    # Make sure base is a power of 2 ( bases 2,3,8 are supported by builtins int conversion)
    if base <= 1:
        raise ValueError("Base must be 2,3 or 8.")
    # Base 10 representation
    if base == 10:
        return str(x)
    # Use built-in int conversion for base 2,3,8
    elif base in [2,3,8]:
        return str(int(x, base))
    else:
        # Use built-in int conversion with floor division for other bases
        x = int(x)
        floor_part = x // base
        remainder = x % base
        return f"{remainder:03d}{base}({floor_part + 1):03d}"

# Unit tests
assert change_base(8, 3) == '22'
assert change_base(7, 2) == '111'
assert change_base(5, 8) == '8'
assert change_base(123, 10) == '1000000003'
assert change_base(-12, 2) == '-11111'
```