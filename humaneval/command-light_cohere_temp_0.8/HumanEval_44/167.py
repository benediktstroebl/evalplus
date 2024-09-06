```python
def change_base(x: int, base: int):
    """
    Change the numerical base of input number x to base base.
    return string representation after conversion.
    base numbers less 10
   
    example: change 8 to 3 returns '22'
    """
    return '{:0<{}d}'.format(x, base)

def test_change_base():
    assert change_base(8, 3) == '22'
    assert change_base(10, 2) == '100'
    assert change_base(100, 5) == '200'
    assert change_base(123, 10) == '1200'
    assert change_base(10, 123) == '12300'
    assert change_base(-5, -2) == '-200'
    assert change_base(1, -123) == '-123'
```
The `change_base` function converts the input number to a string representation using the desired base, and the `test_change_base` function verifies that the function behaves correctly with different inputs.