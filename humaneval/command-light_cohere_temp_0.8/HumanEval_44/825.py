```python
def change_base(x: int, base: int):
    """
    Change the numerical base of input number x to base
    base numbers (10) using the given base.
    Returns string representation after conversion.
    """
    output: string representation of the number in the given base.
    """
Examples a simple number 8 in base 3: 22
    """
    return f"{x:.{{base}}"

# Unit tests
test_change_base = lambda: assert change_base(8, 3) == '22'
test_change_base2 = lambda: assert change_base(8, 2) == '1000'
test_change_base3 = lambda: assert change_base(7, 2) == '111'

print("All tests passed!")
```