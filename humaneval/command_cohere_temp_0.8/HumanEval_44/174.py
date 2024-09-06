```python
def change_base(x, base):
    return str(x).translate(str.maketrans('123456789', f'{base}>{base}>{base}>{base}'))
```

This approach takes advantage of the built-in method `str.translate()` and the optional argument `str.maketrans()` to efficiently change the base of the input number.

The tests correspond to the provided problem's test cases. 

```python
def test_change_base():
    assert change_base(8, 3) == '22'
    assert change_base(8, 2) == '1000'
    assert change_base(7, 2) == '111'

test_change_base()
``` 

The approach assumes the input is a valid integer number and that the target base is a valid integer between 2 and 10.