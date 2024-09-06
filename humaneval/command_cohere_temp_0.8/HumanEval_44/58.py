```python
def change_base(x, base):
    return str(x).translate(str.maketrans('123456789', f'{base}_{base}_{base}123'))
```

This approach uses string translation, which is efficient and works without importing any extra modules. It utilizes the built-in `str.maketrans()` method to create a translation table and then applies `str.translate()` to convert the digits of the input number `x` to the base-specific digits desired. The format for `str.maketrans()` is `source -> target`, where source is `123456789` and target is formatted as `{base}_{base}_{base}123` to convert digits 0-9 to the respective base digits. 

This function efficiently changes the base of the input number to the desired base without importing any additional modules and in a straightforward manner.

Here is a simple test suite for this function:
```python
def test_change_base():
    assert change_base(8, 3) == '22'
    assert change_base(8, 2) == '1000'
    assert change_base(7, 2) == '111'
    assert change_base(10, 5) == '2'
    assert change_base(15, 3) == '221'
```