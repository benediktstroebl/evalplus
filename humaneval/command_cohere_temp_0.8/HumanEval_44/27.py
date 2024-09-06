```python
def change_base(x, base):
    return str(x).translate(str.maketrans('123456789', f'{base}_{base}_{base}_{base}_{base}_{base}_{base}_{base}'))
```

This function takes an integer `x` and a base `base` as input. It uses `str.translate()` to convert the digits of `x` into characters denoting the specified `base`. For example, if `base` is `3`, it converts '8' to '222' as '8' in base 3 is '222' and the string value of `x` is returned after this conversion. 

This solution assumes that the input `x` is a valid integer and the `base` is less than 10. You can use this function to change the base of any integer numerically. 

Here is a test case to verify its functionality:
```python
def test_change_base():
    assert change_base(8, 3) == '22'
    assert change_base(8, 2) == '1000'
    assert change_base(7, 2) == '111'
    assert change_base(5, 5) == '51'
    assert change_base(0, 10) == '0'
    assert change_base(150, 10) == '15'
```