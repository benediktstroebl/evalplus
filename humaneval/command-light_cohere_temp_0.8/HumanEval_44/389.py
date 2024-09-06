```python
def change_base(x: int, base: int) -> str:
    """
    Change the base of integer x to base base and returns string representation.
    """
    x must be an integer
    """
    if base < 2 or base > 36:
        raise ValueError("Invalid base number.")
        
    # Perform the conversion using the reversed exponent formula
    base_pow = [pow(digit, base - 1) for digit in x]
    return str(int(tuple(base_pow)))

# Unit tests
assert change_base(8, 3) == '22'
assert change_base(123, 7) == '111'
assert change_base(5, 4) == '10'
assert change_base(-10, 10) == '-105'
assert change_base(7, -1) == '7'
assert change_base(None, 5) == ''
```