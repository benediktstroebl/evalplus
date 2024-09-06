```python
def change_base(x, base):
    return str(x).translate(str.maketrans('123456789', f'{base}_{base}_{base}123'))
```

This approach uses string translation, which is efficient and works without importing any extra modules. It's also conceptually simple and readable.

The tests could be done like this:
```python
def test_change_base():
    assert change_base(8, 3) == '22'
    assert change_base(8, 2) == '1000'
    assert change_base(7, 2) == '111'
    assert change_base(10, 5) == '2'

test_change_base()
```

Or simply use an integrated test runner, like this:
```bash
python -m pytest
```